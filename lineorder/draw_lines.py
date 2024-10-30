import sys
import numpy as np

from .utils import get_line_eq_coefficients
from .utils import get_intersection_point
from .utils import get_line_eq_value
from .utils import svg_header


def draw_lines(
        input, 
        size_px = 1000,
        line_width_px=0.5,
        title_text="Generated by LineOrder", 
        epsilon = 1e-7,
        align_first = True,
        fit_to_circle = True,
        scale_x = 0.91,
        scale_y = 0.91,
        ):
    """For a given set of straight lines this function will generate
    visual representation SVG file, with all lines and all non-overlapping
    triangles. For the best results, the center of the arrangement must be 
    around the (0,0).

    Arguments:
        `input` -- A set of lines in form: `[[x1, y1, x2, y2], ...]`.
        `size_px` -- Image size (in pixels).
        `line_width_px` -- Line width in pixels.
        `title_text` -- A title text ("Generated by LineOrder" by default).
        `epsilon` -- Triangles with a side shorter than epsilon are not counted.

    Returns a dictionary:
        `status` -- The status of the operation (`OK` or `ERROR: [...]`).
        `svg` -- Resulting SVG file.
        `triangles` -- Non-overlapping triangles [[x1,y1, x2,y2, x3,y3], ...]].
        `upper_bound` -- Theoretical upper bound to the number of the \
            non-overlapping triangles.
        `max_R` -- The maximum distance from the (0,0) to a cross-point.
    """

    # Calculates the line equation coefficients [A, B, C] for every line.
    c = list(map(lambda p: get_line_eq_coefficients(p[0],p[1],p[2],p[3]),input))

    style = ""
    style += "\t\tcircle { stroke:black;stroke-width:" + str(line_width_px)
    style += ";fill:none;stroke-dasharray:5,5; }"
    style += "\t\tline { stroke:black;stroke-width:" + str(line_width_px)
    style += ";vector-effect:non-scaling-stroke; }"
    style += "\t\tpath { fill:#00000055; }"

    svg = svg_header.format(style=style, width_px=size_px, height_px=size_px)

    # This will be the maximum distance from the (0,0) to a cross-point.
    max_R = 0

    # The list of non-overlapping triangles:
    # [ [x1, y1, x2, y2, x3, y3], ... ]
    triangles = []

    # Count the number of non-overlapping triangles.

    count = 0

    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            v1 = get_intersection_point(c[i], c[j])
            if v1 is None: continue
            for k in range(j + 1, len(input)):
                v2 = get_intersection_point(c[i], c[k])
                v3 = get_intersection_point(c[j], c[k])

                if v2 is None: continue
                if v3 is None: continue

                # Triangles with a very small side are skipped.
                if np.linalg.norm(v1-v2) < epsilon: continue
                if np.linalg.norm(v1-v3) < epsilon: continue
                if np.linalg.norm(v2-v3) < epsilon: continue

                max_R = max(max_R, np.linalg.norm(v1))
                max_R = max(max_R, np.linalg.norm(v2))
                max_R = max(max_R, np.linalg.norm(v3))

                is_non_overlapping = True
                for u in range(len(input)):
                    if u in [i,j,k]: continue
                    h1 = get_line_eq_value(c[u], v1)
                    h2 = get_line_eq_value(c[u], v2)
                    h3 = get_line_eq_value(c[u], v3)
                    s1 = np.sign(h1)
                    s2 = np.sign(h2)
                    s3 = np.sign(h3)
                    if (s1 != s2) or (s1 != s3) or (s2 != s3):
                        # Check maybe one of the points is at the line,
                        # while two others are at the same side.
                        if (abs(h1) < epsilon) and (s2 == s3): continue
                        if (abs(h2) < epsilon) and (s1 == s3): continue
                        if (abs(h3) < epsilon) and (s1 == s2): continue
                        # Two points are at the different sides.
                        is_non_overlapping = False
                        break

                if is_non_overlapping:
                    count = count + 1
                    triangles.append(
                        np.array([v1[0], v1[1], v2[0], v2[1], v3[0], v3[1]]))
    
    if fit_to_circle:
        scale_x /= max_R
        scale_y /= max_R

    # Calculate the theoretical upper bound for the number of the 
    # non-overlapping triangles.
    k = len(input)
    upper_bound = 0
    if k % 6 in [3,5]: upper_bound = k * (k - 2) // 3
    if k % 6 in [0,2]: upper_bound = (k + 1) * (k - 3) // 3
    if k % 6 in [1,4]: upper_bound = (k*k - 2*k - 2) // 3

    # Add the info text to the SVG.
    svg += '''
    <text x='20' y='30'>({} lines, {} triangles, {} upper bound)</text>
    <text x='20' y='45'>{}</text>\n
    '''.format(len(input), count, upper_bound, title_text)

    # Calculate the rotation matrix for aligning first line with Ox.
    n0 = [c[0][0], c[0][1]]
    A = np.linalg.inv(np.matrix([[n0[0], -n0[1]], [n0[1], n0[0]]]))
    B = np.linalg.inv(np.matrix([[0, 1], [-1, 0]]))
    S = np.matrix([[-scale_x, 0],[0, scale_y]])
    T = S @ B @ A

    if align_first == False:
        T = np.identity(2)

    svg += "\n"

    # Add triangles to the SVG.
    for t in triangles:
        t1 = (T @ [t[0], t[1]]).tolist()[0]
        t2 = (T @ [t[2], t[3]]).tolist()[0]
        t3 = (T @ [t[4], t[5]]).tolist()[0]
        x = (np.array(t1 + t2 + t3) * size_px + size_px) / 2
        svg += "<path d='M {} {} L {} {} L {} {}' />\n".format(
            x[0], x[1], x[2], x[3], x[4], x[5])

    svg += "\n"

    # Add straight lines, clipped by the circle, to the SVG.
    for i in range(len(input)):
        p1 = np.array([input[i][0], input[i][1]])
        p2 = np.array([input[i][2], input[i][3]])

        p1 = np.array((T @ p1).tolist()[0])
        p2 = np.array((T @ p2).tolist()[0])

        a = p1
        v = p2 - p1

        ax, ay = a[0], a[1]
        vx, vy = v[0], v[1]

        sqrt_arg = (1-ax**2)*vy**2+2*ax*ay*vx*vy+(1-ay**2)*vx**2
        if sqrt_arg < 0:
            continue

        a1 = -(np.sqrt(sqrt_arg)+ay*vy+ax*vx)/(vy**2+vx**2)
        a2 = (np.sqrt(sqrt_arg)-ay*vy-ax*vx)/(vy**2+vx**2)

        r1 = a + a1 * v
        r2 = a + a2 * v

        r1 = (r1 * size_px + size_px) / 2
        r2 = (r2 * size_px + size_px) / 2

        svg += "<line x1='{}' y1='{}' x2='{}' y2='{}' />\n".format(
            r1[0], r1[1], r2[0], r2[1])

    svg += "\n<circle cx='{r}px' cy='{r}px' r='{r}px' />".format(r=size_px/2)
    svg += "\n\n</svg>"

    res = {
        "status" : "OK",
        "svg" : svg,
        "triangles" : triangles,
        "upped_bound" : upper_bound,
        "max_R" : max_R,
    }

    return res