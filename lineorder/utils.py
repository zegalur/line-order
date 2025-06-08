import numpy as np
import copy


def get_line_eq_coefficients(x1, y1, x2, y2):
    """ [x1, y1, x2, y2] -> [A, B, C] from Ax + By + C = 0, where |(A,B)| = 1.
    """
    A = y2 - y1
    B = x1 - x2
    l = np.sqrt(A**2 + B**2)
    C = -(A * x1 + B * y1)
    return [A, B, C] / l


def get_intersection_point(l1, l2):
    """For two given lines, this function calculates their intersection point.
    Throw an error if two lines are parallel.
    """
    a = np.array([[l1[0], l1[1]], [l2[0], l2[1]]])  # [[A1, B1], [A2, B2]]
    b = np.array([-l1[2], -l2[2]])                  # [C1, C2]

    if np.linalg.matrix_rank(a) != 2:
        return None

    return np.linalg.solve(a, b)


def get_line_eq_value(line, point):
    """Returns the value of Ax + By + C.
    """
    return line[0] * point[0] + line[1] * point[1] + line[2]

svg_header = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with LineOrder (https://github.com/zegalur/line-order) -->

<svg
    width="{width_px}px"
    height="{height_px}px"
    viewBox="0 0 {width_px} {height_px}"
    version="1.1"
    xmlns="http://www.w3.org/2000/svg">

    <style>
{style}
    </style>

    <rect width="100%" height="100%" fill="white"/>
    
    '''


def reindex_table(table_in, new_first_row):
    """Renumbering and reordering of a table. In a new table `new_first_row` is
    the first lines (and first row of the table).

    Arguments:
        `table_in` -- a well formed table for `N` lines.
        `new_first_row` -- sets what row will be a new first row (from 1 to N).
    
    Returns the renumbered and reordered table. Returns `None` if the input was 
    incorrect.
    """
    # Check if the input table has any multi-line intersection points.
    for row in table_in:
        for cross_point in row:
            if type(cross_point) is list:
                print("WARNING: reindex_table() doesn't support multiline " + 
                      "cross-points. The original table was returned instead.")
                return copy.deepcopy(table_in)

    N = len(table_in)
    if (new_first_row > N) or (new_first_row < 1):
        return None
    
    result = []
    for line_index, row in enumerate(table_in):
        new_row = []
        for index in row:
            new_row.append((N + index - new_first_row) % N + 1)
        if (line_index + 1) < new_first_row:
            new_row.reverse()
        result.append(new_row)
    
    result = result[-(N - new_first_row + 1):] + result[:(new_first_row - 1)]
    return result


def reverse_order(tab):
    """Reverses the order of lines from 1,2,3,..n to 1,n,n-1,..,2.

    Arguments:
        `tab` -- a well formed table for `N` lines.

    Returns the reversed table.
    """
    # Check if the input table has any multi-line intersection points.
    for row in tab:
        for cross_point in row:
            if type(cross_point) is list:
                print("WARNING: reverse_order() doesn't support multiline " + 
                      "cross-points. The original table was returned instead.")
                return copy.deepcopy(tab)

    indx = lambda l: 1 if l==1 else (len(tab)-l+2)
    return [ 
            [ indx(l) for l in (tab[0] if r == 0 else tab[indx(r+1)-1][::-1]) ] 
        for r in range(len(tab)) ]


def add_1_2_line(tab, cross_12 = False):
    """Adds a line between 1 and 2 to an odd table that makes it 
    almost ideal even configuration.

    Arguments:
        `tab` -- a well formed table for `N` lines.
        `cross_12` -- if `True`, crosses the first and the newly added second line.
                      If `False`, fist and second lines will be parallel.
    
    Returns a newly created `N+1` table.
    """
    # Check if the input table has any multi-line intersection points.
    for row in tab:
        for cross_point in row:
            if type(cross_point) is list:
                print("WARNING: add_1_2_line() doesn't support multiline " + 
                      "cross-points. The original table was returned instead.")
                return copy.deepcopy(tab)

    indx = lambda l: 1 if l==1 else (l+1)
    t1 = [ [indx(l) for l in r] for r in tab ]
    for r in range(1, len(tab)):
        t1[r] = [2] + t1[r]
    if cross_12:
        t1[0] = t1[0] + [2]
    t1.insert(1, list(range(3,len(tab)+2)) + ([1] if cross_12 else []))
    return t1


def table_normal_form(table_in):
    """Converts a table into a 'normal form' table, where every row is a list
    of arrays, and multiline cross-points are not affected.
    
    E.g. `[[3,2], [3,1], [2,1]]` into `[[[3],[2]], [[3],[1]], [[2],[1]]]`."""
    res = []
    for row in table_in:
        new_row = []
        for item in row:
            if isinstance(item, list):
                new_row.append(item.copy())
            else:
                new_row.append([item])
        res.append(new_row)
    return res


def group_by_parallel(table):
    """For a given table this function returns an array of arrays 
    `[g1,g2,..]`. If line `i` and line `j` are in the `ak`, they are parallel. 
    If line `i` and line `j` are in different `am` and `an`, they are not 
    parallel.
    
    Returns `"OK", [result]` for well formed tables.

    Returns `"ERROR: ..", []` for incorrect tables."""
    res = []
    N = len(table)

    # "Flatten" the table rows.
    ntab = table_normal_form(table)
    for i in range(N):
        ntab[i] = sum(ntab[i], [])

    # Create groups.
    for i in range(1, N+1):
        already_in_a_group = False
        for g in res:
            if i in g:
                already_in_a_group = True
                break
        if already_in_a_group:
            continue
        group = [i]
        for j in range(i+1, N+1):
            if (j in ntab[i-1]) == False:
                group.append(j)
        res.append(group)
    
    # Check if all parallel lines are also consecutive.
    for g in res:
        for i in range(len(g)-1):
            if g[i] != (g[i+1] - 1):
                return ("ERROR: Incorrect table. " + 
                        "Parallel lines should be consecutive lines."), []

    return "OK", res


gallery_html_header = """<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <title>{title}</title>
</head>

<style>
    img {{ 
        display:block;
        max-width: 100%;
        height: auto;
        width: auto;
        padding: inherit;
        margin: auto;
    }}

    td {{
        text-align: center;
        vertical-align: middle;
    }}

    p {{
        display:block;
    }}

    table {{
        max-width:"100%";
        margin-left: auto;
        margin-right: auto;
    }}

    h1 {{
        text-align: center;
    }}

    h2 {{
        text-align: center;
    }}

    hr {{
        border: 1px solid lightgray;
        margin-top: 40px;
    }}

    .tab {{
        display:block;
        max-width: 100%;
        height: auto;
        width: auto;
        font-family: 'Courier New', Courier, monospace;
    }}
</style>

<body>

<h1>{header}</h1>

"""
