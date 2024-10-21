import numpy as np


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
    return np.linalg.solve(a, b)


def get_line_eq_value(line, point):
    """Returns the value of Ax + By + C.
    """
    return line[0] * point[0] + line[1] * point[1] + line[2]

svg_header = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>

<svg
    width="{width_px}px"
    height="{height_px}px"
    viewBox="0px 0px {width_px}px {height_px}px"
    version="1.1"
    id="svg1=-body"
    xml:space="preserve"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:svg="http://www.w3.org/2000/svg">

    <style>
{style}
    </style>

    <rect width="100%" height="100%" fill="white"/>
    
    '''