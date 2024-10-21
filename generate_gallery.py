import lineorder

# This script generates the showcase gallery.


entries = {

################################################################################

'triangle_3_rot_symmetry' : {
    'entry_title' : 'Triangle\n(3-rotational symmetry)',
    'entry_table' : [
        [3,2],
        [3,1],
        [2,1],
    ],
    'table_font_size' : "10pt",
    'find_lines_args' : {
        'rotational_symmetry' : 3,
    },
    'draw_plines_args' : {
        'title_text' : 'Triangle',
        'size_px' : 300.0,
    },
    'draw_lines_args' : {
        'title_text' : 'Triangle',
        'size_px' : 300.0,
        'scale_x' : 0.7,
        'scale_y' : 0.7,
    },
},

################################################################################

'pentagram_3_rot_symmetry' : {
    'entry_title' : 'Pentagram\n(5-rotational symmetry)',
    'entry_table' : [
        [5,3,4,2], 
        [3,5,4,1],
        [2,5,1,4],
        [5,2,1,3],
        [4,2,3,1],
    ],
    'table_font_size' : "10pt",
    'find_lines_args' : {
        'rotational_symmetry' : 5,
    },
    'draw_plines_args' : {
        'title_text' : 'Pentagram',
        'size_px' : 300.0,
    },
    'draw_lines_args' : {
        'title_text' : 'Pentagram',
        'size_px' : 300.0,
        'scale_x' : 0.7,
        'scale_y' : 0.7,
    },
},

################################################################################

'kobon9_3_rot_symmetry' : {
    'entry_title' : 'Kobon Triangles (9 lines)\n(3-rotational symmetry)',
    'entry_table' : [
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
    'table_font_size' : "8pt",
    'find_lines_args' : {
        'rotational_symmetry' : 3,
        'ineq_epsilon' : 0.3,
        'ineq_max' : 20.0,
        'min_angle' : 0.2,
    },
    'draw_plines_args' : {
        'title_text' : 'Kobon Triangles',
        'size_px' : 400.0,
    },
    'draw_lines_args' : {
        'title_text' : 'Kobon Triangles',
        'size_px' : 400.0,
    },
},

################################################################################

'9_lines' : {
    'entry_title' : 'An arrangement of 9 lines\nwithout symmetries',
    'entry_table' : [
        [9,8,7,6,5,4,3,2],
        [7,6,8,5,9,3,4,1],
        [5,6,7,8,9,2,4,1],
        [5,6,7,8,9,2,3,1],
        [4,3,6,7,8,2,9,1],
        [4,3,5,7,2,8,9,1],
        [4,3,5,6,2,8,9,1],
        [4,3,5,2,6,7,9,1],
        [4,3,2,5,6,7,8,1],
    ],
    'table_font_size' : "10pt",
    'find_lines_args' : {
        'ineq_epsilon' : 0.3,
        'ineq_max' : 20.0,
        'min_angle' : 0.2,
    },
    'draw_plines_args' : {
        'size_px' : 400.0,
    },
    'draw_lines_args' : {
        'size_px' : 400.0,
    },
},

################################################################################

'kobon21_3_rot_symmetry' : {
    'entry_title' : 'Kobon Triangles (21 lines)\n(3-rotational symmetry)\nby P.Savchuk',
    'entry_table' : [
        [21,15,19,17,20,16,18,13,14,11,12,9,10,7,8,5,6,3,4,2],
        [3,15,5,17,11,21,13,19,7,16,9,14,12,20,10,18,6,8,4,1],
        [2,15,21,17,19,11,16,13,20,14,18,9,12,7,10,5,8,6,1,4],
        [5,15,7,11,6,13,9,17,12,19,14,16,10,21,18,20,8,2,1,3],
        [4,15,2,17,21,11,19,13,16,7,14,9,20,12,18,10,3,8,1,6],
        [7,15,11,4,13,17,9,19,12,16,14,21,10,20,18,2,8,3,1,5],
        [6,15,4,11,17,13,21,19,2,16,5,14,20,9,18,12,3,10,1,8],
        [9,11,10,13,12,15,14,17,16,19,18,21,20,4,2,6,3,5,1,7],
        [8,11,15,13,4,17,6,19,21,16,2,14,5,20,7,18,3,12,1,10],
        [11,8,13,15,12,17,14,19,16,4,21,6,20,2,18,5,3,7,1,9],
        [10,8,9,15,6,4,7,17,2,21,5,19,3,16,20,13,18,14,1,12],
        [13,8,15,10,17,4,19,6,16,21,14,2,20,5,18,7,3,9,1,11],
        [12,8,10,15,9,4,6,17,7,21,2,19,5,16,3,20,11,18,1,14],
        [15,8,17,10,19,4,16,6,21,12,2,9,5,7,20,3,18,11,1,13],
        [14,8,12,10,13,9,11,6,7,4,5,2,3,21,1,19,20,17,18,16],
        [17,8,19,10,4,14,6,12,21,9,2,7,5,13,3,11,20,1,18,15],
        [16,8,14,10,12,4,9,6,13,7,11,2,5,21,3,19,1,20,15,18],
        [19,8,21,4,20,6,2,10,5,12,7,9,3,14,11,13,1,16,15,17],
        [18,8,16,10,14,4,12,6,9,21,7,2,13,5,11,3,17,1,15,20],
        [21,8,4,18,6,10,2,12,5,9,7,14,3,13,11,16,1,17,15,19],
        [20,8,18,4,10,6,14,12,16,9,19,7,13,2,11,5,17,3,15,1],
    ],
    'table_font_size' : "8pt",
    'find_lines_args' : {
        'rotational_symmetry' : 3,
    },
    'draw_plines_args' : {
        'title_text' : 'Pavlo Savchuk',
        'size_px' : 600.0,
    },
    'draw_lines_args' : {
        'title_text' : 'Pavlo Savchuk',
        'size_px' : 800.0,
    },
},

################################################################################

'kobon15_5_rot_symmetry' : {
    'entry_title' : 'Kobon Triangles (15 lines)\n(5-rotational symmetry)\nby Toshitaka Suzuki',
    'entry_table' : [
        [15,13,14,11,12,7,9,5,8,6,10,3,4,2,],
        [3,7,5,13,6,11,9,12,8,15,10,14,4,1,],
        [2,7,13,5,11,6,12,9,15,8,14,10,1,4,],
        [5,7,6,13,9,11,8,12,10,15,14,2,1,3,],
        [4,7,2,13,3,11,15,12,14,9,1,8,10,6,],
        [7,4,13,2,11,3,12,15,9,14,8,1,10,5,],
        [6,4,5,2,3,13,15,11,14,12,1,9,10,8,],
        [9,13,11,4,12,2,15,3,14,6,1,5,10,7,],
        [8,13,4,11,2,12,3,15,6,14,5,1,7,10,],
        [11,13,12,4,15,2,14,3,1,6,5,8,7,9,],
        [10,13,8,4,9,2,6,3,5,15,7,14,1,12,],
        [13,10,4,8,2,9,3,6,15,5,14,7,1,11,],
        [12,10,11,8,9,4,6,2,5,3,7,15,1,14,],
        [15,4,2,10,3,8,6,9,5,12,7,11,1,13,],
        [14,4,10,2,8,3,9,6,12,5,11,7,13,1,],
    ],
    'table_font_size' : "8pt",
    'find_lines_args' : {
        'rotational_symmetry' : 5,
        'ineq_epsilon' : 0.3,
    },
    'draw_plines_args' : {
        'title_text' : 'Toshitaka Suzuki',
        'size_px' : 600.0,
    },
    'draw_lines_args' : {
        'title_text' : 'Toshitaka Suzuki',
        'size_px' : 800.0,
    },
},

################################################################################

'kobon7_no_sym' : {
    'entry_title' : 'Kobon Triangles\n7 lines without symmetries',
    'entry_table' : [
        [2,3,4,6,5,7,],
        [1,3,6,4,7,5,],
        [1,2,6,7,4,5,],
        [1,6,2,7,3,5,],
        [6,1,7,2,3,4,],
        [5,1,4,2,3,7,],
        [1,5,2,4,3,6,],
    ],
    'table_font_size' : "10pt",
    'find_lines_args' : {
        'ineq_epsilon' : 0.3,
        'ineq_max' : 20.0,
        'min_angle' : 0.2,
    },
    'draw_plines_args' : {
        'size_px' : 400.0,
    },
    'draw_lines_args' : {
        'size_px' : 400.0,
    },
},

################################################################################

'9_no_sym_20tri' : {
    'entry_title' : '9 lines without symmetries',
    'entry_table' : [
        [2,3,4,8,6,7,5,9,],
        [1,3,8,4,7,6,9,5,],
        [1,2,8,9,7,6,4,5,],
        [1,8,2,7,9,6,3,5,],
        [6,8,7,1,9,2,3,4,],
        [5,8,1,7,2,9,4,3,],
        [8,5,1,6,2,4,9,3,],
        [7,5,6,1,4,2,3,9,],
        [1,5,2,6,4,7,3,8,],
    ],
    'table_font_size' : "10pt",
    'find_lines_args' : {
        'ineq_epsilon' : 0.3,
        'ineq_max' : 20.0,
        'min_angle' : 0.2,
    },
    'draw_plines_args' : {
        'size_px' : 400.0,
    },
    'draw_lines_args' : {
        'size_px' : 400.0,
    },
},

################################################################################

# add your entries here ...

}


ERROR_PNG_FILENAME = "gallery/imgs/error.svg"

gallery_html = """<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <title>LineOrder Gallery</title>
</head>

<style>
    img { 
        display:block;
        max-width: 100%;
        height: auto;
        width: auto;
        padding: inherit;
        margin: auto;
    }

    td {
        text-align: center;
        vertical-align: middle;
    }

    p {
        display:block;
    }

    table {
        max-width:"100%";
        margin-left: auto;
        margin-right: auto;
    }

    h1 {
        text-align: center;
    }

    h2 {
        text-align: center;
    }

    hr {
        border: 1px solid lightgray;
        margin-top: 40px;
    }

    .tab {
        display:block;
        max-width: 100%;
        height: auto;
        width: auto;
        font-family: 'Courier New', Courier, monospace;
    }
</style>

<body>

<h1>LineOrder Gallery</h1>

"""

entry_template = """
<hr>
<h2>{entry_title}</h2>
<table>
    <colgroup>
        <col span="1" style="width: 20%;">
        <col span="1" style="width: 40%;">
        <col span="1" style="width: 40%;">
    </colgroup>
    <tbody>
        <tr>
            <td><pre class='tab' style='font-size:{f_size};'>{table}</pre></td>
            <td><img src="{plines_svg_fname}" /></td>
            <td><img src="{lines_svg_fname}" /></td>
        </tr>
    </tbody>
</table>
"""

for key, entry in entries.items():
    entry_table = entry['entry_table']
    print("Generating " + key + " ...")

    # Generate pseudolines SVG

    pseudolines_svg_filename = ERROR_PNG_FILENAME
    pseudolines_svg = lineorder.draw_pseudolines(
        entry_table, **entry['draw_plines_args'])
    
    if pseudolines_svg['status'] == 'OK':
        pseudolines_svg_filename = "imgs/" + key + "_pseudolines.svg"
        with open("gallery/" + pseudolines_svg_filename, "w") as text_file:
            text_file.write(pseudolines_svg['svg'])

    # Get a straightened arrangement

    result = lineorder.find_lines(entry_table, **entry['find_lines_args'])
    lines_svg_filename = ERROR_PNG_FILENAME

    if result['status'] == 'OK':
        result_svg = lineorder.draw_lines(
            result['lines'], **entry['draw_lines_args'])
        
        if result_svg['status'] == 'OK':
            lines_svg_filename = "imgs/" + key + "_lines.svg"
            with open("gallery/" + lines_svg_filename, "w") as text_file:
                text_file.write(result_svg['svg'])
    
    # Add this entry to the gallery
    gallery_html += entry_template.format(
        entry_title = entry['entry_title'].replace("\n","<br>"),
        table = str(entry_table).replace("],","],<br>").replace(", ",","),
        plines_svg_fname = pseudolines_svg_filename,
        lines_svg_fname = lines_svg_filename,
        f_size = entry['table_font_size'],
        )


# Create gallery HTML file
gallery_html += "\n<hr>\n\n</body>\n"
with open("gallery/index.html", "w") as text_file:
    text_file.write(gallery_html)

