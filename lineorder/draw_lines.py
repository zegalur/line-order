import sys
import numpy as np
import math

from .utils import get_line_eq_coefficients
from .utils import get_intersection_point
from .utils import get_line_eq_value
from .utils import svg_header


# Applies simple exponential "fish-eye" projection:
def exp_proj(p,c,R,factor):
    if np.linalg.norm(np.array(p) - np.array(c)) >= R:
        return [ p[0], p[1] ]
    x = (p[0] - c[0]) / R
    y = (p[1] - c[1]) / R
    r = min(1.0, math.sqrt(x*x + y*y))
    r2 = r ** factor
    scale = r2 / r if r != 0 else 1
    x2 = x * scale
    y2 = y * scale
    return [x2 * R + c[0], y2 * R + c[1]]


# Projects a point according to a given (complex) fish-eye projection:
def project(p, c, R, projection, factor, local_fisheyes, local_factor):
    if np.linalg.norm(np.array(p) - np.array(c)) >= R:
        return [ p[0], p[1] ]

    if projection == 'exponential':
        r0 = exp_proj(p,c,R,factor)
        res = np.array(r0)
        for count,cx,cy,radius in local_fisheyes:
            r1 = exp_proj(r0,[cx,cy],radius,local_factor)
            dr = np.array(r1) - np.array(r0)
            res += dr
        return [res[0], res[1]]

    if projection == 'spherical':
        x = (p[0] - c[0]) / R
        y = (p[1] - c[1]) / R
        r = min(1.0, math.sqrt(x*x + y*y))
        theta = math.atan(r)
        strength = factor# * math.pi / 2.0
        r2 = math.sin(theta * strength) / math.sin(strength)
        scale = (r2 / r) if r != 0 else 1
        s2 = math.sin(math.atan(1.0) * strength) / math.sin(strength)
        x2 = x * scale / s2
        y2 = y * scale / s2
        return [x2 * R + c[0], y2 * R + c[1]]

    else:
        return None


# Returns SVG block for a line for a given projection:
def get_line(
        delta_l, 
        p1, p2, center, 
        fisheye, projection, factor, 
        local_fisheyes, local_factor,
        ):
    if fisheye == False:
        return "<line x1='{}' y1='{}' x2='{}' y2='{}' />\n".format(
            p1[0], p1[1], p2[0], p2[1])

    res = "<!-- line ({},{}) to ({},{}) -->\n".format(p1[0],p1[1], p2[0],p2[1])

    R = center[0]
    r0 = project(
            [p1[0],p1[1]], center, R, projection, factor, 
            local_fisheyes, local_factor)
    d = "M{},{}".format(r0[0], r0[1])
    p = p1
    l0 = np.linalg.norm(p2 - p1)
    dp = (p2 - p1) / l0
    last_r = p1
    while np.linalg.norm(p - p1) <= l0:
        delta = 0.0
        step = 1.0 / l0
        r = project(p, center, R, projection, factor, 
                    local_fisheyes, local_factor)
        while True:
            n_p = p + dp * (delta + step)
            n_r = np.array(project(n_p, center, R, projection, factor, 
                                   local_fisheyes, local_factor))
            pl = np.linalg.norm(n_r - last_r)
            if pl > delta_l:
                step /= 2.0
            else:
                delta += step
                r = n_r
                p = n_p
                step *= 2.0
            if step < 0.00001:
              break
        d += " L{},{}".format(r[0], r[1])
        last_r = r

    res += '<path class="line" d="{}" />\n'.format(d)
    return res


# Returns SVG block for a triangle for a given projection:
def get_tri(
        seg_count, 
        t1,t2,t3, 
        center, 
        fisheye, projection, factor,
        local_fisheyes, local_factor,
        ):
    if fisheye == False:
        return "<path d='M {} {} L {} {} L {} {}' />\n".format(
                    t1[0],t1[1], t2[0],t2[1], t3[0],t3[1])

    SEGMENTS = seg_count
    d = ""
    first = True
    R = center[0]
    for p1,p2 in [(t1,t2), (t2,t3), (t3,t1)]:
      if first:
        r = project([p1[0], p1[1]], center, R, projection, factor, 
                    local_fisheyes, local_factor)
        d += "M{},{} ".format(r[0], r[1])
        first = False
      for i in range(1, SEGMENTS + 1):
        a = i / SEGMENTS
        px = p1[0] * (1.0 - a) + p2[0] * a
        py = p1[1] * (1.0 - a) + p2[1] * a
        r = project([px,py], center, R, projection, factor, 
                    local_fisheyes, local_factor)
        d += "L{},{} ".format(r[0], r[1])
    d += "z"
    res = '<path d="{}" />\n'.format(d)
    return res


# Returns incircle of given triangle:
def get_incircle(t1,t2,t3, center, fisheye, projection, factor):
    R = center[0]
    p = [ np.array(project(t,center,R,projection,factor,[],factor) if fisheye else t) 
          for t in [t1,t2,t3] ]
    
    # triangle side lengths:
    a = np.linalg.norm(p[2] - p[1])
    b = np.linalg.norm(p[2] - p[0])
    c = np.linalg.norm(p[1] - p[0])

    # incenter coordinates:
    x = (a * p[0][0] + b * p[1][0] + c * p[2][0]) / (a + b + c)
    y = (a * p[0][1] + b * p[1][1] + c * p[2][1]) / (a + b + c)

    # inradius
    s = (a + b + c) / 2.0
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    r = area / s

    return (x,y,r,area,a,b,c)


# Filters and clusterizes a set of incircles:
def filter_and_clusterize(
        incircles, max_radius, cluster_radius, cluster_final_radius):
    clusters = []
    assigned = {}
    for i in range(len(incircles)):
        if i in assigned:
            continue
        x, y, r, area, a, b, c = incircles[i]
        if r > max_radius: 
            continue

        assigned[i] = True
        c = np.array([x,y])
        points = [ np.array([x,y]) ]

        for j in range(i + 1, len(incircles)):
            if j in assigned:
                continue
            nx,ny,nr,narea,na,nb,nc = incircles[j]
            if nr > max_radius:
                continue
            p = np.array([nx,ny])
            if np.linalg.norm(c - p) < cluster_radius:
                points.append(p)
                c = np.mean(points,axis=0)
                assigned[j] = True

        clusters.append((len(points), c[0],c[1], cluster_final_radius))
    return clusters


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
        show_upper_bound = True,

        fisheye = False,
        projection = "exponential",
        factor = 1.0,
        local_fisheyes = [], # (skip,cx,cy,r)
        local_factor = 1.0,
        tri_seg_count = 100,
        delta_l = 1.5,

        incircles = False,
        draw_incircles = False,

        clusterize = False,
        min_radius = -2.0,
        cluster_radius = -20.0,
        cluster_final_radius = -20.0,
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
        `fisheye` -- When `True`, applies `fisheye` distortion effect.
        `projection` -- Fish-eye projection type. Possible values are: \
                `exponential` (default), `spherical`.
        `factor` -- fish-eye factor (default 1.0).
        `tri_seg_count` -- triangles precision for fish-eye projection \
                (`100` by default).
        `delta_l` -- line segment length for fish-eye projection, in pixels \
                (`1.5` by default).
        `incircles` -- when `True`, computes incircles of projected triangles.
        `draw_incircles` -- when `True`, draws triangle incircles.

    Returns a dictionary:
        `status` -- The status of the operation (`OK` or `ERROR: [...]`).
        `svg` -- Resulting SVG file.
        `triangles` -- Non-overlapping triangles [[x1,y1, x2,y2, x3,y3], ...]].
        `upper_bound` -- Theoretical upper bound to the number of the \
            non-overlapping triangles.
        `max_R` -- The maximum distance from the (0,0) to a cross-point.
        `incircles` -- when `incircles=True`, contains an array of all \
            incircles of projected triangles in a form \
            `[(cx,cy,r,area,a,b,c), ...]`, where `a,b,c` - sides.
        `clusters` -- when `clusterize=True`, contains an array of clusters: \
            `[(count, cx, cy, radius), ...]`

    """

    if projection not in ['exponential', 'spherical']:
        return { 'status': "ERROR: unknown projection type `{}`.".format(
                    projection) }

    # Calculates the line equation coefficients [A, B, C] for every line.
    c = list(map(lambda p: get_line_eq_coefficients(p[0],p[1],p[2],p[3]),input))

    style = ""
    style += "\t\tcircle { stroke:black;stroke-width:" + str(line_width_px)
    style += ";fill:none;stroke-dasharray:5,5; }\n"
    style += "\t\tline { stroke:black;stroke-width:" + str(line_width_px)
    style += ";vector-effect:non-scaling-stroke; }\n"
    style += "\t\tpath { fill: #000000; fill-opacity: 0.33; }\n"

    if fisheye:
        style += "\t\tpath.line { fill:none"
        style += ";stroke:black;stroke-width:" + str(line_width_px)
        style += ";vector-effect:non-scaling-stroke; }\n"

    if draw_incircles:
        style += "\t\tcircle.incircle { stroke:DarkSlateGrey;stroke-width:" + str(2*line_width_px)
        style += ";fill:LightGreen;stroke-dasharray:0; }\n"

    if clusterize:
        style += "\t\tcircle.cluster { stroke:red;stroke-width:" + str(2*line_width_px)
        style += ";fill:none;stroke-dasharray:0; }\n"

    svg = svg_header.format(
            style=style, 
            width_px=int(size_px), 
            height_px=int(size_px),
            )

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
        if max_R == 0:
            # No cross-points were found. 
            # Fit all the line input points instead.
            for l in input:
                max_R = max(max_R, np.linalg.norm([l[0],l[1]]))
                max_R = max(max_R, np.linalg.norm([l[2],l[3]]))
        scale_x /= max_R
        scale_y /= max_R

    # Calculate the theoretical upper bound for the number of the 
    # non-overlapping triangles.
    k = len(input)
    upper_bound = 0
    if k % 6 in [3,5]: upper_bound = k * (k - 2) // 3
    if k % 6 in [0,2]: upper_bound = (k + 1) * (k - 3) // 3
    if k % 6 in [1,4]: upper_bound = (k*k - 2*k - 2) // 3
    if k % 2 == 0:
        # Improved upper bound for even k:
        upper_bound = math.floor(k * (k - 7/3) / 3)

    # Add the info text to the SVG.
    if show_upper_bound:
        svg += '''
        <text x='20' y='30'>({} lines, {} triangles, {} upper bound)</text>
        <text x='20' y='45'>{}</text>\n
        '''.format(len(input), count, upper_bound, title_text)
    else:
        svg += '''
        <text x='20' y='30'>({} lines, {} triangles)</text>
        <text x='20' y='45'>{}</text>\n
        '''.format(len(input), count, title_text)

    # Calculate the rotation matrix for aligning first line with Ox.
    n0 = [c[0][0], c[0][1]]
    A = np.linalg.inv(np.matrix([[n0[0], -n0[1]], [n0[1], n0[0]]]))
    B = np.linalg.inv(np.matrix([[0, 1], [-1, 0]]))
    S = np.matrix([[-scale_x, 0],[0, scale_y]])
    T = S @ B @ A

    if align_first == False:
        T = np.identity(2)

    svg += "\n"

    circles = []

    # Add triangles to the SVG.
    for t in triangles:
        t1 = (T @ [t[0], t[1]]).tolist()[0]
        t2 = (T @ [t[2], t[3]]).tolist()[0]
        t3 = (T @ [t[4], t[5]]).tolist()[0]
        x = (np.array(t1 + t2 + t3) * size_px + size_px) / 2
        svg += get_tri(tri_seg_count,
                       [x[0],x[1]], [x[2],x[3]], [x[4],x[5]],
                       [size_px/2, size_px/2],
                       fisheye, projection, factor, 
                       local_fisheyes, local_factor)
        if incircles:
            circles.append(get_incircle(
                       [x[0],x[1]], [x[2],x[3]], [x[4],x[5]],
                       [size_px/2, size_px/2],
                       fisheye, projection, factor))

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

        svg += get_line(
                delta_l,
                r1,r2, [size_px/2, size_px/2], 
                fisheye, projection, factor, 
                local_fisheyes, local_factor)

    # draw incircles if needed:
    clusters = []
    if draw_incircles:
        min_r = size_px
        svg += "\n"
        for x,y,r,area,a,b,c in circles:
            svg += "\n<circle class='incircle' cx='{}' cy='{}' r='{}' />".format(x,y,r)
            if r < min_r:
                min_r = r
        svg += "\n"

        # draw clusters
        if clusterize:
            if min_radius < 0.0:
                min_radius = -min_radius * min_r
            if cluster_radius < 0.0:
                cluster_radius = -cluster_radius * min_r
            if cluster_final_radius < 0.0:
                cluster_final_radius = -cluster_final_radius * min_r
            clusters = filter_and_clusterize(
                    circles, min_radius, cluster_radius, cluster_final_radius)
            svg += "\n"
            for count,cx,cy,r in clusters:
                svg += "\n<circle class='cluster' cx='{}' cy='{}' r='{}' />".format(
                        cx, cy, r)
                if min_r > r:
                    r = min_r
            svg += "\n"


    svg += "\n<circle cx='{r}' cy='{r}' r='{r}' />".format(r=int(size_px/2))
    svg += "\n\n</svg>"

    res = {
        "status" : "OK",
        "svg" : svg,
        "triangles" : triangles,
        "upper_bound" : upper_bound,
        "max_R" : max_R,
        "incircles" : circles,
        "clusters" : clusters,
    }

    return res
