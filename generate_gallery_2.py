import numpy as np
from fractions import Fraction

import lineorder

# This script generates the second showcase gallery.

entries = {

################################################################################

'ibase_kobon_5' : {
    'table' : [
        [5,3,4,2], 
        [3,5,4,1],
        [2,5,1,4],
        [5,2,1,3],
        [4,2,3,1],
    ],
    'first_row' : 1,
    'title' : "Kobon 5-Lines<br>(5 Triangles, Mirror Symmetry)",
    'font_size' : "10pt",
    'eps_denominator' : 2 * 5,
    'eps_eq' : 1e-8,
    'round_values_to' : 7,
    'find_lines_args' : {
        "mirrored" : True,
    },
    'draw_lines_args' : {
        'size_px' : 400.0,
    },
},

################################################################################

'ibase_kobon_7' : {
    'table' : [
        [2,3,4,6,5,7,],
        [1,3,6,4,7,5,],
        [1,2,6,7,4,5,],
        [1,6,2,7,3,5,],
        [6,1,7,2,3,4,],
        [5,1,4,2,3,7,],
        [1,5,2,4,3,6,],
    ],
    'first_row' : 3,
    'title' : "Kobon 7-Lines<br>(11 Triangles, Mirror Symmetry)",
    'font_size' : "10pt",
    'eps_denominator' : 2 * 7,
    'eps_eq' : 1e-8,
    'round_values_to' : 7,
    'find_lines_args' : {
        "mirrored" : True,
    },
    'draw_lines_args' : {
        'size_px' : 400.0,
    },
},

################################################################################

'ibase_kobon_9' : {
    'table' : [
        [9,3,7,5,8,4,6,2],
        [3,9,5,7,4,8,6,1],
        [2,9,1,7,8,5,6,4],
        [5,9,7,2,8,1,6,3],
        [4,9,2,7,1,8,3,6],
        [7,9,8,2,1,4,3,5],
        [6,9,4,2,5,1,3,8],
        [9,6,2,4,1,5,3,7],
        [8,6,7,4,5,2,3,1],
    ],
    'first_row' : 3,
    'title' : "Kobon 9-Lines<br>(21 Triangles, Mirror Symmetry)",
    'font_size' : "10pt",
    'eps_denominator' : 2 * 9,
    'eps_eq' : 1e-8,
    'round_values_to' : 7,
    'find_lines_args' : {
        "mirrored" : True,
    },
    'draw_lines_args' : {
        'size_px' : 400.0,
    },
},

################################################################################

'ibase_11' : {
    'table' : [
        [3,2,5,4,7,6,11,9,10,8],
        [3,1,5,11,7,10,6,9,4,8],
        [2,1,11,5,10,7,9,6,8,4],
        [5,1,7,11,6,10,9,2,8,3],
        [4,1,2,11,3,10,9,7,8,6],
        [7,1,11,4,10,2,9,3,8,5],
        [6,1,4,11,2,10,3,9,5,8],
        [9,11,10,1,2,4,3,6,5,7],
        [8,11,1,10,4,2,6,3,7,5],
        [11,8,1,9,4,6,2,7,3,5],
        [10,8,9,1,6,4,7,2,5,3],
    ],
    'first_row' : 3,
    'title' : "11-Lines (32 Triangles)<br>(not suitable for Proposition 3.1)",
    'font_size' : "10pt",
    'eps_denominator' : 2 * 11,
    'eps_eq' : 1e-8,
    'round_values_to' : 7,
    'find_lines_args' : {
    },
    'draw_lines_args' : {
        'size_px' : 400.0,
    },
},

################################################################################

'ibase_kobon_13' : {
    'table' : [
        [13,9,11,10,12,7,8,3,5,4,6,2],
        [3,9,4,10,7,13,8,11,5,12,6,1],
        [2,9,13,10,11,7,12,8,1,5,6,4],
        [9,2,10,13,7,11,8,12,5,1,6,3],
        [9,7,10,8,13,11,2,12,4,1,3,6],
        [7,9,8,10,11,13,12,2,1,4,3,5],
        [6,9,5,10,2,13,4,11,3,12,1,8],
        [9,6,10,5,13,2,11,4,12,3,1,7],
        [8,6,7,5,4,2,3,13,1,11,12,10],
        [6,8,5,7,2,4,13,3,11,1,12,9],
        [6,13,5,2,8,4,7,3,10,1,9,12],
        [13,6,2,5,4,8,3,7,1,10,9,11],
        [12,6,11,5,8,2,7,4,10,3,9,1],
    ],
    'first_row' : 1,
    'title' : "Kobon 13-Lines<br>(47 Triangles, Mirror Symmetry)",
    'font_size' : "10pt",
    'eps_denominator' : 2 * 13,
    'eps_eq' : 1e-8,
    'round_values_to' : 7,
    'find_lines_args' : {
        "mirrored" : True,
    },
    'draw_lines_args' : {
        'size_px' : 400.0,
        'scale_x' : 3.0,
        'title_text' : '(X scaled by 1/3)'
    },
},

################################################################################

# ... your entry here ...

}

ERROR_PNG_FILENAME = "gallery/imgs/error.svg"

gallery_html = lineorder.gallery_html_header.format(
    title="LineOrder Gallery #2", header="LineOrder Gallery #2")

entry_template = """
<hr>
<h2>{entry_title}</h2>
<table>
    <colgroup>
        <col span="1" style="width: 40%;">
        <col span="1" style="width: 60%;">
    </colgroup>
    <tbody>
        <tr>
            <td style='text-align:center;'><pre class='tab' 
                style='font-size:{f_size}; text-align:left;'>
{data}
                </pre></td>
            <td><img src="{lines_svg_fname}" /></td>
        </tr>
    </tbody>
</table>
"""


for key, entry in entries.items():
    print("Generating '{}'...".format(key))

    table = entry['table']
    table = lineorder.reindex_table(table, entry['first_row'])

    eps = 1 / entry['eps_denominator']

    result = lineorder.find_lines(
        table, 
        fixed_first_line_segments=True, 
        first_line_segment_epsilon=eps,
        **entry['find_lines_args'])

    N = len(table)
    EPS = entry['eps_eq']
    ROUND = entry['round_values_to']

    epss = [("-&epsilon;", -eps), ("&epsilon;", eps)]
    seg_1 = [(-i, np.tan(-i * np.pi / (N - 1))) for i in reversed(range(1,(N-1)//2))]
    seg_3 = [( i, np.tan( i * np.pi / (N - 1))) for i in range(1,(N-1)//2)]
    tangents = seg_1 + seg_3

    if result['status'] == 'OK':
        i = 0

        maxima = ""
        data = "y = m<sub>i</sub>(x - a<sub>i</sub>), i = 0..{}:\n\n".format(N-1)
        data += "&epsilon; = 1 / {} < 1 / {}\n\n".format(entry['eps_denominator'], 2*(N-1))

        for line in result['lines_ac']:
            mi = -np.cos(line[0]+np.pi/2) / np.sin(line[0]+np.pi/2)
            ai = -line[1] / np.cos(line[0]+np.pi/2)
            mi = round(mi, ROUND)

            error = True
            if abs(mi) + abs(ai) < EPS:
                data += "m<sub>{i}</sub> = 0, a<sub>{i}</sub> = 0\n".format(i = i)
                maxima += "0,\n"
                error = False

            for (k, val) in tangents:
                if abs(val - ai) < EPS:
                    data += "m<sub>{i}</sub> = {mi}, a<sub>{i}</sub> = tan({n}&#x1D70B;/{d})\n".format(
                        i=i, mi = mi, n=k, d=(N-1))
                    maxima += "{mi} * (x - tan({n} * %pi / {d})),\n".format(
                        i=i, mi = mi, n=k, d=(N-1))
                    error = False
                    break

            for (str, val) in epss:
                if abs(val - ai) < EPS:
                    data += "m<sub>{i}</sub> = {mi}, a<sub>{i}</sub> = {str}\n".format(
                        i=i, mi = mi, str=str)
                    if val < 0:
                        maxima += "{mi} * (x - 1/{d}),\n".format(i=i, mi=mi,d=(2*N))
                    else:
                        maxima += "{mi} * (x + 1/{d}),\n".format(i=i, mi=mi,d=(2*N))
                    error = False
                    break

            if error:
                data += "line {} : ERROR values!\n".format(i)

            i += 1

        data += "\n\nFor wxMaxima:\n" + maxima
        data = data.replace("\n", "<br>")

        result_svg = lineorder.draw_lines(
            result['lines'], **entry['draw_lines_args'])
        svg_filename = "imgs/{}.svg".format(key)

        with open("gallery/" + svg_filename, "w") as text_file:
            text_file.write(result_svg['svg'])
            entry_html = entry_template.format(
                entry_title=entry['title'], 
                f_size=entry['font_size'],
                data=data, 
                lines_svg_fname=svg_filename)
            gallery_html += entry_html


# Create gallery HTML file
gallery_html += "\n<hr>\n\n</body>\n"
with open("gallery/index_2.html", "w") as text_file:
    text_file.write(gallery_html)