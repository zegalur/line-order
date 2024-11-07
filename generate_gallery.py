import lineorder

# This script generates the showcase gallery.


# 15-lines arrangement, first discovered by Suzuki.
kobon_15 = [
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
]


kobon = {

################################################################################

'triangle_3_rot_symmetry' : {
    'entry_title' : '3-Line Solution (1 Triangle)',
    'entry_table' : [
        [3,2],
        [3,1],
        [2,1],
    ],
    'first_row' : 1,
    'table_font_size' : "10pt",
    'find_lines_args' : {
        'rotational_symmetry' : 3,
    },
    'draw_plines_args' : {
        'size_px' : 300.0,
    },
    'draw_lines_args' : {
        'size_px' : 300.0,
        'scale_x' : 0.7,
        'scale_y' : 0.7,
    },
},

################################################################################

'kobon_4' : {
    'entry_title' : '4-Line Solution #1 (2 Triangles)',
    'entry_table' : [
        [4,3],
        [3,4],
        [2,4,1],
        [2,3,1],
    ],
    'first_row' : 1,
    'table_font_size' : "10pt",
    'find_lines_args' : {
        'mirrored' : True,
    },
    'draw_plines_args' : {
        'size_px' : 300.0,
    },
    'draw_lines_args' : {
        'size_px' : 300.0,
        'scale_x' : 6.0,
        'scale_y' : 0.5,
    },
},

################################################################################

'kobon_4_2' : {
    'entry_title' : '4-Line Solution #2 (2 Triangles)',
    'entry_table' : [
        [4,3,2],
        [[3,4],1],
        [[4,2],1],
        [[2,3],1],
    ],
    'first_row' : 1,
    'table_font_size' : "10pt",
    'find_lines_args' : {
        'mirrored' : True,
    },
    'draw_plines_args' : {
        'size_px' : 300.0,
    },
    'draw_lines_args' : {
        'size_px' : 300.0,
        'epsilon' : 1e-4, 
        'scale_x' : 0.65,
    },
},

################################################################################

'pentagram_5_rot_symmetry' : {
    'entry_title' : '5-Line Solution (5 Triangles)',
    'entry_table' : [
        [5,3,4,2], 
        [3,5,4,1],
        [2,5,1,4],
        [5,2,1,3],
        [4,2,3,1],
    ],
    'first_row' : 1,
    'table_font_size' : "10pt",
    'find_lines_args' : {
        'rotational_symmetry' : 5,
    },
    'draw_plines_args' : {
        'size_px' : 300.0,
    },
    'draw_lines_args' : {
        'size_px' : 300.0,
        'scale_x' : 0.7,
        'scale_y' : 0.7,
    },
},

################################################################################

'kobon_6_1' : {
    'entry_title' : '6-Line Solution #1 (7 Triangles)',
    'entry_table' : [
        [6,4,5,3],
        [4,[3,6],5],
        [4,[6,2],5,1],
        [3,2,6,1,5],
        [6,2,3,1,4],
        [5,[2,3],4,1],
    ],
    'first_row' : 1,
    'table_font_size' : "10pt",
    'find_lines_args' : {
        'mirrored' : True,
        'ineq_max' : 1.0,
        'ineq_epsilon' : 0.2,
    },
    'draw_plines_args' : {
        'size_px' : 300.0,
    },
    'draw_lines_args' : {
        'epsilon' : 1e-4, 
        'size_px' : 300,
        'scale_y' : 0.8,
    },
},

################################################################################

'kobon_6_2' : {
    'entry_title' : '6-Line Solution #2 (7 Triangles)',
    'entry_table' : [
        [[3,4],[2,5],6],
        [3,4,[5,1],6],
        [2,[4,1],[5,6]],
        [2,[1,3],6,5],
        [[1,2],[6,3],4],
        [1,2,[3,5],4],
    ],
    'first_row' : 1,
    'table_font_size' : "10pt",
    'find_lines_args' : {
        'rotational_symmetry' : 3,
    },
    'draw_plines_args' : {
        'size_px' : 300.0,
    },
    'draw_lines_args' : {
        'epsilon' : 1e-4, 
        'size_px' : 300,
        'scale_x' : 0.8,
        'scale_y' : 0.8,
    },
},

################################################################################

'kobon_7' : {
    'entry_title' : '7-Line Solution (11 Triangles)',
    'entry_table' : [
        [2,3,4,6,5,7,],
        [1,3,6,4,7,5,],
        [1,2,6,7,4,5,],
        [1,6,2,7,3,5,],
        [6,1,7,2,3,4,],
        [5,1,4,2,3,7,],
        [1,5,2,4,3,6,],
    ],
    'first_row' : 3,
    'table_font_size' : "10pt",
    'find_lines_args' : {
        'ineq_epsilon' : 0.13,
        'mirrored' : True,
    },
    'draw_plines_args' : {
        'size_px' : 400.0,
    },
    'draw_lines_args' : {
        'size_px' : 400.0,
    },
},

################################################################################

'kobon_8' : {
    'entry_title' : '8-Line Solution (15 Triangles)',
    'entry_table' : [
        [8,6,7,4,5,2,3],
        [6,[4,8],7,5,1,3],
        [4,6,5,7,8,1,2],
        [3,6,[8,2],7,1,5],
        [6,3,[7,8],2,1,4],
        [5,3,4,2,8,1,7],
        [3,[8,5],2,4,1,6],
        [3,[5,7],[2,4],6,1],
    ],
    'first_row' : 1,
    'table_font_size' : "10pt",
    'find_lines_args' : {
    },
    'draw_plines_args' : {
        'size_px' : 400.0,
    },
    'draw_lines_args' : {
        'size_px' : 400.0,
        'epsilon' : 1e-4, 
    },
},

################################################################################

'kobon_9_3_rot_symmetry' : {
    'entry_title' : '9-Line Solution (21 Triangles)',
    'entry_table' : [
        [9,7,8,5,6,3,4,2],
        [3,7,5,9,6,8,4,1],
        [2,7,9,5,8,6,1,4],
        [5,7,6,9,8,2,1,3],
        [4,7,2,9,3,8,1,6],
        [7,4,9,2,8,3,1,5],
        [6,4,5,2,3,9,1,8],
        [9,4,2,6,3,5,1,7],
        [8,4,6,2,5,3,7,1],
    ],
    'first_row' : 1,
    'table_font_size' : "8pt",
    'find_lines_args' : {
        'rotational_symmetry' : 3,
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

'kobon_10_25tri_wajnberg' : {
    'entry_title' : '10-Line Solution (25 Triangles) by Wajnberg',
    'entry_table' : [
        [10,8,9,6,7,4,5,3],
        [8,[4,10],6,7,[3,9],5],
        [4,8,6,10,7,[9,2],5,1],
        [3,8,[10,2],6,9,7,1,5],
        [6,8,7,10,9,2,3,1,4],
        [5,8,3,10,2,4,9,1,7],
        [8,5,10,3,2,9,4,1,6],
        [7,5,6,3,4,2,10,1,9],
        [10,5,[2,3],7,4,6,1,8],
        [9,5,7,3,6,[2,4],8,1],
    ],
    'first_row' : 1,
    'table_font_size' : "8pt",
    'find_lines_args' : {
        'mirrored' : True,
        'ineq_epsilon' : 0.3,
        'ineq_max' : 20.0,
        'min_angle' : 0.2,
    },
    'draw_plines_args' : {
        'title_text' : "by Wajnberg",
        'size_px' : 400.0,
    },
    'draw_lines_args' : {
        'title_text' : "by Wajnberg",
        'size_px' : 400.0,
        'epsilon' : 1e-4, 
    },
},

################################################################################

'kobon_11_32tri' : {
    'entry_title' : '11-Line Solution (32 Triangles) by Honma',
    'entry_table' : [
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
    'table_font_size' : "10pt",
    'find_lines_args' : {
        'ineq_max' : 4.0,
    },
    'draw_plines_args' : {
        'size_px' : 400.0,
        'title_text' : "by Honma",
    },
    'draw_lines_args' : {
        'size_px' : 400.0,
        'title_text' : "by Honma",
    },
},

################################################################################

'kobon_12_38tri' : {
    'entry_title' : '12-Line Solution (38 Triangles) by Kabanovitch',
    'entry_table' : [
        [12,5,[9,11],7,10,[4,6],8,2,3],
        [5,12,7,9,4,11,6,10,8,1,3],
        [5,4,7,6,9,8,11,10,12,1,2],
        [5,3,7,12,9,2,11,10,[6,1],8],
        [4,3,2,12,1,11,9,10,7,8,6],
        [7,3,9,12,11,2,10,[1,4],8,5],
        [6,3,4,12,2,9,11,1,10,5,8],
        [9,3,11,12,10,2,1,4,6,5,7],
        [8,3,6,12,4,2,7,[11,1],5,10],
        [11,3,12,8,2,6,4,1,7,5,9],
        [10,3,8,12,6,2,4,7,[1,9],5],
        [3,10,8,11,6,9,4,7,2,5,1],
    ],
    'first_row' : 3,
    'table_font_size' : "10pt",
    'find_lines_args' : {
        'ineq_max' : 4.0,
    },
    'draw_plines_args' : {
        'title_text' : "by Kabanovitch",
        'size_px' : 400.0,
    },
    'draw_lines_args' : {
        'title_text' : "by Kabanovitch",
        'size_px' : 400.0,
        'epsilon' : 1e-4,
    },
},

################################################################################

'kobon_13_m_sym_47tri' : {
    'entry_title' : '13-Line Solution (47 Triangles) by Kabanovitch',
    'entry_table' : [
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
    'table_font_size' : "10pt",
    'find_lines_args' : {
        'mirrored' : True,
    },
    'draw_plines_args' : {
        'title_text' : "by Kabanovitch",
        'size_px' : 400.0,
    },
    'draw_lines_args' : {
        'title_text' : "by Kabanovitch",
        'size_px' : 400.0,
    },
},

################################################################################

'kobon_14_53tri' : {
    'entry_title' : '14-Line Solution (53 Triangles) by Johannes Bader',
    'entry_table' : [
        [14,12,13,7,10,6,9,3,8,5,11,4],
        [3,7,5,6,4,10,9,12,8,13,11,14],
        [2,7,12,6,13,10,14,9,1,8,11,5],
        [5,7,6,2,10,12,9,13,8,14,11,1],
        [4,7,2,6,12,10,13,9,14,8,1,11,3],
        [7,4,2,5,12,3,13,14,10,1,9,11,8],
        [6,4,5,2,3,12,14,13,1,10,11,9],
        [9,10,12,2,13,4,14,5,1,3,11,6],
        [8,10,2,12,4,13,5,14,3,1,6,11,7],
        [8,9,2,4,12,5,13,3,14,6,1,7,11],
        [12,13,2,14,4,1,5,3,8,6,9,7,10],
        [11,8,2,9,4,10,5,6,3,7,14,1,13],
        [11,2,8,4,9,5,10,3,6,14,7,1,12],
        [2,11,4,8,5,9,3,10,6,13,7,12,1],
    ],
    'first_row' : 1,
    'table_font_size' : "10pt",
    'find_lines_args' : {
    },
    'draw_plines_args' : {
        'title_text' : "by Johannes Bader",
        'size_px' : 400.0,
    },
    'draw_lines_args' : {
        'title_text' : "by Johannes Bader",
        'size_px' : 500.0,
    },
},

################################################################################

'kobon_15_5_rot_symmetry' : {
    'entry_title' : '15-Line Solution (65 Triangles, 5-rotational symmetry)'+
                    ' by Toshitaka Suzuki',
    'entry_table' : kobon_15,
    'first_row' : 1,
    'table_font_size' : "8pt",
    'find_lines_args' : {
        'rotational_symmetry' : 5,
        'ineq_epsilon' : 0.3,
    },
    'draw_plines_args' : {
        'title_text' : 'by Toshitaka Suzuki',
        'size_px' : 600.0,
    },
    'draw_lines_args' : {
        'title_text' : 'by Toshitaka Suzuki',
        'size_px' : 600.0,
    },
},

################################################################################

'kobon_16_72tri' : {
    'entry_title' : ('16-Line Solution (72 Triangles, ' + 
                     'based on 15-line solution by ' + 
                     'Toshitaka Suzuki) by Johannes Bader'),
    'entry_table' : [
        [16,14,15,12,13,8,10,6,9,7,11,4,5,3,],
        [3,4,5,6,7,8,9,10,11,12,13,14,15,16,],
        [2,4,8,6,14,7,12,10,13,9,16,11,15,5,1,],
        [2,3,8,14,6,12,7,13,10,16,9,15,11,1,5,],
        [2,6,8,7,14,10,12,9,13,11,16,15,3,1,4,],
        [2,5,8,3,14,4,12,16,13,15,10,1,9,11,7,],
        [2,8,5,14,3,12,4,13,16,10,15,9,1,11,6,],
        [2,7,5,6,3,4,14,16,12,15,13,1,10,11,9,],
        [2,10,14,12,5,13,3,16,4,15,7,1,6,11,8,],
        [2,9,14,5,12,3,13,4,16,7,15,6,1,8,11,],
        [2,12,14,13,5,16,3,15,4,1,7,6,9,8,10,],
        [2,11,14,9,5,10,3,7,4,6,16,8,15,1,13,],
        [2,14,11,5,9,3,10,4,7,16,6,15,8,1,12,],
        [2,13,11,12,9,10,5,7,3,6,4,8,16,1,15,],
        [2,16,5,3,11,4,9,7,10,6,13,8,12,1,14,],
        [2,15,5,11,3,9,4,10,7,13,6,12,8,14,1,],
    ],
    'first_row' : 1,
    'table_font_size' : "8pt",
    'find_lines_args' : {
    },
    'draw_plines_args' : {
        'title_text' : 'by Johannes Bader (based on 15-line solution by ' + 
                        'Toshitaka Suzuki)',
        'size_px' : 600.0,
    },
    'draw_lines_args' : {
        'title_text' : 'by Johannes Bader (based on 15-line solution by ' + 
                        'Toshitaka Suzuki)',
        'size_px' : 800.0,
    },
},

################################################################################

'kobon_17_85tri' : {
    'entry_title' : '17-Line Solution (85 Triangles) by Johannes Bader',
    'entry_table' : [
        [2,6,4,12,5,8,3,10,7,14,11,13,9,16,15,17],
        [1,6,12,4,14,8,16,10,13,5,11,7,17,9,15,3],
        [4,6,5,12,8,1,10,14,7,13,11,16,9,17,15,2],
        [3,6,1,12,2,14,16,8,13,10,17,11,15,7,9,5],
        [6,3,12,1,8,14,10,16,13,2,11,17,7,15,9,4],
        [5,3,4,1,2,12,16,14,17,13,15,10,11,8,9,7],
        [8,12,10,1,14,3,13,16,11,2,17,5,15,4,9,6],
        [7,12,3,1,5,14,2,16,4,13,17,10,15,11,6,9],
        [10,12,11,14,13,1,16,3,17,2,15,5,4,7,6,8],
        [9,12,7,1,3,14,5,16,2,13,4,17,8,15,6,11],
        [12,9,14,1,13,3,16,7,2,5,17,4,15,8,6,10],
        [11,9,10,7,8,3,5,1,4,2,6,16,17,14,15,13],
        [14,9,1,11,3,7,16,5,2,10,4,8,17,6,15,12],
        [13,9,11,1,7,3,10,5,8,2,4,16,6,17,12,15],
        [16,1,17,3,2,9,5,7,4,11,8,10,6,13,12,14],
        [15,1,9,3,11,7,13,5,10,2,8,4,14,6,12,17],
        [1,15,3,9,2,7,5,11,4,10,8,13,6,14,12,16],
    ],
    'first_row' : 1,
    'table_font_size' : "8pt",
    'find_lines_args' : {
    },
    'draw_plines_args' : {
        'title_text' : 'by Johannes Bader',
        'size_px' : 600.0,
    },
    'draw_lines_args' : {
        'title_text' : 'by Johannes Bader',
        'size_px' : 800.0,
    },
},

################################################################################

'kobon_18_93tri' : {
    'entry_title' : '18-Line Solution (93 Triangles) by Johannes Bader',
    'entry_table' : [
        [18,17,16,13,15,7,12,5,10,9,14,6,11,4,8,3],
        [3,5,4,7,6,13,9,17,10,12,8,15,11,16,14,18],
        [2,5,17,7,13,4,16,9,12,6,15,10,18,11,14,8,1],
        [5,2,7,17,13,3,16,18,12,15,9,10,6,14,11,1,8],
        [4,2,3,17,18,13,16,7,15,12,1,10,14,9,11,6,8],
        [7,2,13,17,9,16,12,3,15,18,10,4,14,1,11,5,8],
        [6,2,4,17,3,13,18,16,5,15,1,12,14,10,11,9],
        [9,13,10,17,12,2,15,16,11,18,14,3,1,4,5,6],
        [8,13,2,17,6,16,3,12,18,15,4,10,1,14,5,11,7],
        [13,8,17,2,12,16,15,3,18,6,4,9,1,5,14,7,11],
        [13,12,17,15,2,16,8,18,3,14,4,1,6,5,9,7,10],
        [13,11,17,8,2,10,16,6,3,9,18,4,15,5,1,7,14],
        [12,11,10,8,9,2,6,17,4,3,7,18,5,16,1,15],
        [15,17,16,2,18,8,3,11,4,6,1,9,5,10,7,12],
        [14,17,11,2,8,16,10,3,6,18,9,4,12,5,7,1,13],
        [17,14,2,11,8,15,10,12,6,9,3,4,18,7,5,13,1],
        [16,14,15,11,12,8,10,2,9,6,13,4,7,3,5,18,1],
        [2,14,8,11,3,10,6,15,9,12,4,16,7,13,5,17,1],
    ],
    'first_row' : 1,
    'table_font_size' : "8pt",
    'find_lines_args' : {
        #'rotational_symmetry' : 3,
    },
    'draw_plines_args' : {
        'title_text' : 'by Johannes Bader',
        'size_px' : 600.0,
    },
    'draw_lines_args' : {
        'title_text' : 'by Johannes Bader',
        'size_px' : 800.0,
    },
},

################################################################################

'kobon_21_133tri_1' : {
    'entry_title' : '21-Line Solution #1 (133 Triangles, ' + 
                    '3-rotational symmetry) by P.Savchuk',
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
    'first_row' : 1,
    'table_font_size' : "8pt",
    'find_lines_args' : {
        'rotational_symmetry' : 3,
    },
    'draw_plines_args' : {
        'title_text' : 'by Pavlo Savchuk',
        'size_px' : 600.0,
    },
    'draw_lines_args' : {
        'title_text' : 'by Pavlo Savchuk',
        'size_px' : 800.0,
    },
},

################################################################################

'kobon_21_133tri_2' : {
    'entry_title' : '21-Line Solution #2 (133 Triangles, ' + 
                    '3-rotational symmetry) by P.Savchuk',
    'entry_table' : [
        [2,4,3,6,5,8,7,10,9,12,11,14,13,18,16,20,17,19,15,21,],
        [1,4,8,6,20,10,18,12,14,9,16,7,19,11,21,13,17,5,15,3,],
        [4,1,6,8,5,10,7,12,9,20,14,18,11,16,13,19,17,21,15,2,],
        [3,1,2,8,20,6,18,10,21,14,16,12,19,9,17,11,13,7,15,5,],
        [6,1,8,3,10,20,12,18,9,14,7,16,11,19,13,21,17,2,15,4,],
        [5,1,3,8,2,20,4,18,21,10,16,14,19,12,17,9,13,11,15,7,],
        [8,1,10,3,12,20,9,18,14,5,16,2,19,21,11,17,13,4,15,6,],
        [7,1,5,3,6,2,4,20,21,18,19,16,17,14,15,12,13,10,11,9,],
        [10,1,12,3,20,7,18,5,14,2,16,21,19,4,17,6,13,15,11,8,],
        [9,1,7,3,5,20,2,18,4,21,6,16,19,14,17,12,15,13,8,11,],
        [12,1,14,20,18,3,16,5,19,2,21,7,17,4,13,6,15,9,8,10,],
        [11,1,9,3,7,20,5,18,2,14,21,16,4,19,6,17,10,15,8,13,],
        [14,1,18,20,16,3,19,5,21,2,17,7,4,11,6,9,15,10,8,12,],
        [13,1,11,20,3,18,7,5,9,2,12,21,4,16,6,19,10,17,8,15,],
        [16,18,17,20,19,1,21,3,2,5,4,7,6,11,9,13,10,12,8,14,],
        [15,18,1,20,13,3,11,5,7,2,9,21,12,4,14,6,10,19,8,17,],
        [18,15,20,1,19,3,21,5,2,13,7,11,4,9,6,12,10,14,8,16,],
        [17,15,16,1,13,20,11,3,14,7,9,5,12,2,10,4,6,21,8,19,],
        [20,15,1,17,3,13,5,11,2,7,21,9,4,12,6,14,10,16,8,18,],
        [19,15,17,1,16,13,18,11,14,3,9,7,12,5,10,2,6,4,8,21,],
        [1,15,3,17,5,13,2,11,7,19,9,16,12,14,4,10,6,18,8,20,],
    ],
    'first_row' : 8,
    'table_font_size' : "8pt",
    'find_lines_args' : {
        'rotational_symmetry' : 3,
    },
    'draw_plines_args' : {
        'title_text' : 'by Pavlo Savchuk',
        'size_px' : 600.0,
    },
    'draw_lines_args' : {
        'title_text' : 'by Pavlo Savchuk',
        'size_px' : 800.0,
    },
},

################################################################################

'kobon_25_191tri' : {
    'entry_title' : '25-Line Solution (191 Triangles, Mirror Symmetry). ' +
                    'Table by Kyle Wood',
    'entry_table' : [
        [2,8,4,12,6,10,7,11,5,9,3,14,13,24,18,22,16,20,17,21,15,23,19,25],
        [1,8,24,12,22,10,20,11,21,9,23,14,25,13,18,4,16,6,17,7,15,5,19,3],
        [4,8,6,12,7,10,5,11,9,1,14,24,13,22,18,20,16,21,17,23,15,25,19,2],
        [3,8,1,12,24,10,22,11,20,9,21,14,23,13,25,18,2,16,17,6,15,7,19,5],
        [6,8,7,12,10,3,11,1,9,24,14,22,13,20,18,21,16,23,17,25,15,2,19,4],
        [5,8,3,12,1,10,24,11,22,9,20,14,21,13,23,18,25,16,2,17,4,15,19,7],
        [8,5,12,3,10,1,11,24,9,22,14,20,13,21,18,23,16,25,17,2,15,4,19,6],
        [7,5,6,3,4,1,2,24,25,22,23,20,21,12,18,11,17,14,19,13,16,10,15,9],
        [10,12,11,3,1,5,24,7,22,6,20,4,21,2,23,25,14,18,13,17,16,19,15,8],
        [9,12,5,3,7,1,6,24,4,22,2,20,25,21,23,11,18,14,17,13,19,16,8,15],
        [12,9,3,5,1,7,24,6,22,4,20,2,21,25,23,10,18,8,17,19,14,16,13,15],
        [11,9,10,5,7,3,6,1,4,24,2,22,25,20,23,21,8,18,19,17,16,14,15,13],
        [14,1,24,3,22,5,20,7,21,6,23,4,25,2,18,9,17,10,19,8,16,11,15,12],
        [13,1,3,24,5,22,7,20,6,21,4,23,2,25,9,18,10,17,8,19,11,16,12,15],
        [16,18,17,22,20,24,21,1,23,3,25,5,2,7,4,6,19,9,8,10,11,13,12,14],
        [15,18,24,22,1,20,3,21,5,23,7,25,6,2,4,17,9,19,10,8,13,11,14,12],
        [18,15,22,24,20,1,21,3,23,5,25,7,2,6,4,16,9,13,10,14,8,11,19,12],
        [17,15,16,24,1,22,3,20,5,21,7,23,6,25,4,2,13,9,14,10,11,8,12,19],
        [20,22,21,24,23,1,25,3,2,5,4,7,6,15,9,16,10,13,8,14,11,17,12,18],
        [19,22,15,24,17,1,16,3,18,5,13,7,14,6,9,4,11,2,10,25,12,23,8,21],
        [22,19,24,15,1,17,3,16,5,18,7,13,6,14,4,9,2,11,25,10,23,12,8,20],
        [21,19,20,15,17,24,16,1,18,3,13,5,14,7,9,6,11,4,10,2,12,25,8,23],
        [24,19,1,15,3,17,5,16,7,18,6,13,4,14,2,9,25,11,10,21,12,20,8,22],
        [23,19,21,15,20,17,22,16,18,1,13,3,14,5,9,7,11,6,10,4,12,2,8,25],
        [1,19,3,15,5,17,7,16,6,18,4,13,2,14,9,23,11,21,10,20,12,22,8,24]
    ],
    'first_row' : 1,
    'table_font_size' : "8pt",
    'find_lines_args' : {
        'mirrored' : True,
    },
    'draw_plines_args' : {
        'size_px' : 600.0,
    },
    'draw_lines_args' : {
        'size_px' : 800.0,
        'scale_x' : 3.0,
    },
},

################################################################################

'kobon_29_261tri' : {
    'entry_title' : '29-Line Solution (261 Triangles). [Savchuk]\n' +
                    'Autogenerated, using gen_2nm1(kobon_15), ' +
                    'based on solution by Suzuki',
    'entry_table' : lineorder.gen_2nm1(
                        lineorder.reindex_table(kobon_15, 2))['table'],
    'first_row' : 1,
    'table_font_size' : "6pt",
    'find_lines_args' : {
    },
    'draw_plines_args' : {
        'size_px' : 700.0,
    },
    'draw_lines_args' : {
        'size_px' : 1000.0,
        'scale_x' : 2.5,
    },
},

################################################################################

'kobon_33_341tri' : {
    'entry_title' : '33-Line Solution (341 Triangles, Mirror Symmetry). ' + 
                    '[Savchuk]\nAutogenerated, using ' + 
                    'gen_2nm1_repeat([[3,2],[3,1],[2,1]], count=4)',
    'entry_table' : lineorder.gen_2nm1_repeat(
                        [[3,2],[3,1],[2,1]], count=4)['table'],
    'first_row' : 1,
    'table_font_size' : "6pt",
    'find_lines_args' : {
        'mirrored' : True,
        'ineq_epsilon' : 0.005,
    },
    'draw_plines_args' : {
        'size_px' : 800.0,
    },
    'draw_lines_args' : {
        'size_px' : 1400.0,
        'scale_x' : 2.5,
    },
},

################################################################################

# add your entries here ...

}


other = {

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
    'first_row' : 1,
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
    'first_row' : 1,
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
            <td><pre class='tab' style='font-size:{f_size}; text-align:left;'>{table}</pre></td>
            <td><img src="{plines_svg_fname}" /></td>
            <td><img src="{lines_svg_fname}" /></td>
        </tr>
    </tbody>
</table>
"""

def generate_std_gallery(entries, html_name, title):
    print("Generating `{}.html`...".format(html_name))

    gallery_html = lineorder.gallery_html_header.format(
        title=title, header=title)

    for key, entry in entries.items():
        print("    Generating " + key + " ...")
        entry_table = entry['entry_table']
        entry_table = lineorder.reindex_table(entry_table, entry['first_row'])

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
        
        table_str = "["
        for row in entry_table:
            table_str += "["
            for cross_point in row:
                table_str += str(cross_point).replace(", ",",") + ","
            table_str = table_str[:-1] + "],<br> "
        table_str = table_str[:-6] + "]"

        # Add this entry to the gallery
        gallery_html += entry_template.format(
            entry_title = entry['entry_title'].replace("\n","<br>"),
            table = table_str,
            plines_svg_fname = pseudolines_svg_filename,
            lines_svg_fname = lines_svg_filename,
            f_size = entry['table_font_size'],
            )


    # Create gallery HTML file
    gallery_html += "\n<hr>\n\n</body>\n"
    with open("gallery/" + html_name + ".html", "w") as text_file:
        text_file.write(gallery_html)

    print("...DONE\n")

################################################################################

generate_std_gallery(
    kobon, "kobon", "LineOrder Gallery #1<br>Kobon triangle problem")

generate_std_gallery(
    other, "other", "LineOrder Gallery #3<br>Other Examples")