import copy
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

from .utils import get_line_eq_coefficients

# Normalized Ax + By + C = 0 into `a`, where A=cos(a), B=sin(a)
def get_line_angle(B): 
    return (np.pi/2 - np.arccos(B))


def solver(
        input,
        test_lines,

        rotational_symmetry,
        mirrored,

        do_tests,
        show_plots,

        ineq_epsilon,
        ineq_max,

        min_angle,
        max_angle,

        main_coefficient,
        angles_coefficient,

        maxiter,
        ftol,
        minimize_method,
        ):
    """(see `find_lines` and `test_lines` for more information)
    """

    result = { 
        'status' : 'OK', 
        'warnings' : '', 
        }

    # Rotational symmetry
    S = 1 if mirrored else rotational_symmetry

    # The number of lines
    N = len(input) 

    # Period
    P = 1 + (N // 2) if mirrored else N // S 

    # Test related variables
    test_eq = np.zeros((N, 3))
    test_variables = np.zeros((N, 2))
    test_result = np.zeros(2 * N)
    test_line_scale = 1.0

    if do_tests:

        # Convert test lines into a list of angles + signed distances (a, C)
        # such that for every Ax + By + C = 0, A = cos(a), B = sin(a).

        for i in range(N):
            l = test_lines
            test_eq[i] = get_line_eq_coefficients(l[i][0], l[i][1], l[i][2], l[i][3])
        for i in range(N):
            a = get_line_angle(test_eq[i][1])
            test_variables[i][0], test_variables[i][1] = a, test_eq[i][2]
            test_result[2*i], test_result[2*i+1] = a, test_eq[i][2]
        
        result['test_line_equations'] = copy.deepcopy(test_eq)
        result['test_line_angles'] = copy.deepcopy(test_variables)

        # Draw result lines so we can visually check if everything is OK.
        # Big points are first points of the test lines.

        if show_plots:
            xs = np.linspace(-1.3 * test_line_scale, 1.3 * test_line_scale)
            fig,ax = plt.subplots()
            for i in range(N):
                ax.plot(xs, (-np.cos(test_variables[i][0])*xs - test_variables[i][1]) 
                        / np.sin(test_variables[i][0]), label=("line " + str(i+1)))
                ax.scatter([test_lines[i][0] * test_line_scale], 
                        [test_lines[i][1] * test_line_scale])
            ax.scatter([0], [0])
            plt.legend(loc="upper left")
            ax.set_xlim((-1.3 * test_line_scale, 1.3 * test_line_scale)) 
            ax.set_ylim((-1.3 * test_line_scale, 1.3 * test_line_scale))
            plt.title("Test lines (big points are first points of test lines)")
            plt.show()

    test_table = ""

    # This solver will try to find a set of lines in a form of:
    # (ai, Ci), where `x*cos(ai) + y*sin(ai) + Ci = 0` is i-th line.
    # See README.md for a brief description of the method.

    # This sets the tolerance on how close/far a two consecutive cross-points 
    # on the same line can be:
    INEQ_EPS = ineq_epsilon
    INEQ_MAX = ineq_max

    # Sets the tolerance toward the min and max angles 
    # between two neighboring lines.
    MIN_A = min_angle
    MAX_A = max_angle * np.pi / (N - 1)

    def cmp_func(row, l1, l2):
        if l1 < row: l1 += N
        if l2 < row: l2 += N
        return l1 < l2

    # "Sign-correction" function (see README.md)
    def get_s(row, l1, l2):
        s = 1.0 if l1 > l2 else -1.0
        s *= -1.0 if cmp_func(row, l1, l2) else 1.0
        return s

    # Checks if a given set of test lines satisfy a system of inequalities 
    # that specify the correct ordering of cross-points.

    if do_tests:
        for i in range(N):
            test_table += '\n'
            for m in range(N-2):
                j = input[i][m] - 1
                k = input[i][m+1] - 1

                # Calculate F(row, l1, l2)

                s = get_s(i+1, j+1, k+1)

                ai, ci = test_variables[i][0], test_variables[i][1]
                aj, cj = test_variables[j][0], test_variables[j][1]
                ak, ck = test_variables[k][0], test_variables[k][1]

                F = 0.0
                F += ci * np.sin(ak - aj)
                F += cj * np.sin(ai - ak)
                F += ck * np.sin(aj - ai)

                # If a given three lines intersect each other in the correct 
                # order, the F-values must be less than zero:
                test_table += '1' if (F * s) < 0 else '0'

        if test_table.find('0') != -1:
            err_msg = "ERROR: Incorrect test table!"
            err_msg += "\nThis table must be all 1's:\n"
            err_msg += test_table
            err_msg += "\n0 is for F-values that are >= 0."
            result['status'] = err_msg
            return result

    # Tolerance function for `x < v` condition. 
    def less_than(x, v):
        if x < v: return 0.0
        return (x - v) ** 2

    # For i-th line this return (ai*, Ci*) considering all symmetries.
    # i -> (ai, Ci)
    def get_ac(x, i): 
        if mirrored:
            j = i if i < P else (N - i)
            a0, aj, cj = x[0], x[2*j], x[2*j + 1]
            a = aj if i < P else (2 * a0 - aj - np.pi)
            c = cj if i < P else -cj
            return (a, c)
        else:
            C_sign = 1.0 if (i // P) % 2 == 0 else -1.0
            a_delta = (i // P) * (np.pi / S)
            j = i % P
            return (x[2*j] - a_delta, C_sign * x[2*j + 1])

    # A minimum of this target function is a possible solution.
    def target_fun(x):
        res = 0.0
        
        # Calculates how much the inequalities for correct order of 
        # cross-points were violated.

        for i in range(P):
            for m in range(N-2):
                j = input[i][m] - 1
                k = input[i][m+1] - 1
                
                # Calculate F(row, l1, l2)

                s = get_s(i+1, j+1, k+1)
                
                (ai, ci) = get_ac(x, i)
                (aj, cj) = get_ac(x, j)
                (ak, ck) = get_ac(x, k)
                
                val = 0
                val += ci * np.sin(ak - aj)
                val += cj * np.sin(ai - ak)
                val += ck * np.sin(aj - ai)

                # -INEQ_MAX < F(row, l1, l2) < -INEQ_EPS < 0
                res += (less_than( val * s, -INEQ_EPS)) * main_coefficient
                res += (less_than(-val * s,  INEQ_MAX)) * main_coefficient

        # Calculates how much the angle related inequalities were violated.

        # ai < a0 (first line angle is the biggest angle)
        for i in range(N):
            (a0, c0) = get_ac(x, 0)
            (ai, ci) = get_ac(x, i)
            res += less_than(ai, a0) * angles_coefficient

        # Other angle constrains.
        for i in range(P):
            (ai, ci) = get_ac(x, i)
            (aj, cj) = get_ac(x, i + 1)

            # The angle between two consecutive lines are in [MIN_A, MAX_A]
            res += less_than(aj + MIN_A, ai) * angles_coefficient
            res += less_than(ai, aj + MAX_A) * angles_coefficient
            if i > 0:
                (ak, ck) = get_ac(x, i - 1)
                res += less_than(ai + MIN_A, ak) * angles_coefficient
            
        # The angle between the first and last lines is greater than MIN_A.
        (a0, c0) = get_ac(x, 0)
        (aN, cN) = get_ac(x, N - 1)
        res += less_than(a0 - np.pi, aN + MIN_A) * angles_coefficient

        return res

    if do_tests:
        result['target_func_value'] = target_fun(test_result)
        if result['target_func_value'] > 1e-6:
            result['warnings'] += "WARNING: "
            result['warnings'] += "Target function value for test lines "
            result['warnings'] += "is not small enough.\n"

    # Initial guess for the arrangement.
    # [ a1, C1, a2, C2, ... ]
    x0 = np.zeros(2*P)
    for i in range(P):
        x0[2*i] = np.pi/2 - i * np.pi / N
        x0[2*i+1] = (-0.1 if (i % 2) == 0 else 0.1)

    # Set the bounding conditions:
    #        0 <= ai <= pi/S
    #   -100.0 <= Ci <= 100.0
    bounds = []
    for i in range(P):
        bounds.append((0, np.pi / S))
        bounds.append((-100.0, 100.0)) # (-1.0, 1.0)


    # Minimize the target function.
    res = minimize(target_fun, x0=x0, bounds=bounds, method=minimize_method,
                    options={'ftol': ftol, 'maxiter': maxiter})
    result['minimize_result'] = res

    # Draws a given lines (ai, Ci), only slightly rotated.
    def draw_lines(data, scale, title):
        # draw result lines
        x = np.linspace(-scale, scale)
        fig,ax = plt.subplots()
        da = 0.05
        for i in range(N):
            (ai, ci) = get_ac(data, i)
            ai += da
            ax.plot(x, (-np.cos(ai)*x - ci) / np.sin(ai), label=("line "+str(i+1)))
        plt.legend(loc="upper left")
        ax.set_xlim((-scale, scale))
        ax.set_ylim((-scale, scale))
        ax.scatter([0], [0])
        plt.title(title)
        plt.show()

    if do_tests and show_plots:
        draw_lines(test_result, 1.3 * test_line_scale, 
            "This lines must be the same as the test lines, only slightly rotated")

    if show_plots:
        draw_lines(x0, 10.0, "Initial guess (x0)")
        draw_lines(res.x, 10.0, "Minimization result")

    # Get result lines as [ x1,y1, x2,y2 ]
    result['lines'] = []
    for i in range(N):
        (ai, ci) = get_ac(res.x, i)
        n = np.array([np.cos(ai), np.sin(ai)])
        d = ci
        v = np.array([-n[1], n[0]])
        p1 = (n*d - v) * 300.0
        p2 = (n*d + v) * 300.0
        result['lines'].append([p1[0], p1[1], p2[0], p2[1]])

    return result


def test_and_find_lines(
        input_table,
        test_lines,

        rotational_symmetry = 1,
        mirrored = False,

        show_plots = False,

        ineq_epsilon = 0.01,
        ineq_max = 1000.0,

        min_angle = 0.1,
        max_angle = 4.0,

        main_coefficient = 10.0,
        angles_coefficient = 0.01,

        maxiter = 13000,
        ftol = 1e-14,
        minimize_method = 'L-BFGS-B',
        ):
    """This function attempts to find a set of straight lines that corresponds 
    to a given arrangement of pseudolines, where each pair intersects at 
    distinct points specified in a table. Additionally, it evaluates how well 
    a set of test lines matches the pseudoline arrangement and computes 
    the target function value for the test lines.

    Arguments:
        `input_table` -- A table of the arrangement.
        `test_lines` -- A set of test lines in form: `[[x1, y1, x2, y2], ...]`

        `rotational_symmetry` -- Rotational symmetry (1 meaning no symmetry)
        `mirrored` -- Mirror symmetry (if `True` - skips the rot. symmetry). \
            Mirrored by (1 + N // 2, 2 + N // 2) pair (by a perpendicular line \
            to the first line).

        `show_plots` -- If `True`, will show results in pop-up windows.

        `ineq_epsilon` -- Sets how much the inequalities for the proper \
            ordering of lines must be less than 0 (this sets the tolerance on \
            how close a two consecutive cross-points on the same line can be).
        `ineq_max` -- This sets the the tolerance on how far away a two cross \
            points on the same line can be.

        `min_angle` -- Sets the tolerance toward the min angle between \
            two neighboring lines.
        `max_angle` -- Sets the tolerance toward the max angle between \
            two neighboring lines (4.0, 2.0, 1.0 are all good values to try).
            
        `main_coefficient` -- Sets the weight in the target function for the \
            intolerance to the cross-points related violations. \
            (10.0 or 1.0 are good values to try)
        `angles_coefficient` -- Sets the weight in the target function for the \
            intolerance to the angles related violations.

        `maxiter` -- `maxiter` parameter for `minimize`.
        `ftol` -- `ftol` parameter for `minimize`.
        `minimize_method` -- `method` parameter for `minimize`.

    Returns a dictionary:
        `status` -- Status of the operation (`OK` or `ERROR: [...]`).
        `warnings` -- Any relevant warning or empty string.
        `lines` -- Resulting lines in a form: `[[x1, y1, x2, y2], ...]`.

        `target_func_value` -- Target function value for test lines. Ideally \
            this value must be equal to zero or very close to zero.
        `test_line_equations` -- Test line equation coefficients [[A,B,C],...] \
            for each test line (Ax + By + C = 0).
        `test_line_angles` -- Test line angles and signed distances [ai, Ci], \
            for each test line, where `x*cos(ai) + y*sin(ai) + Ci = 0`.

        `minimize_result` -- full result from the `minimize` function.
    """
    return solver(copy.deepcopy(input_table), 
                  copy.deepcopy(test_lines),

                  rotational_symmetry = rotational_symmetry,
                  mirrored = mirrored,
                  
                  do_tests = True,
                  show_plots = show_plots,

                  ineq_epsilon = ineq_epsilon,
                  ineq_max = ineq_max,

                  min_angle = min_angle,
                  max_angle = max_angle,

                  main_coefficient = main_coefficient,
                  angles_coefficient = angles_coefficient,

                  maxiter = maxiter,
                  ftol = ftol,
                  minimize_method = minimize_method,
                  )


def find_lines(
        input_table,

        rotational_symmetry = 1,
        mirrored = False,

        show_plots = False,

        ineq_epsilon = 0.01,
        ineq_max = 1000.0,

        min_angle = 0.1,
        max_angle = 4.0,

        main_coefficient = 10.0,
        angles_coefficient = 0.01,

        maxiter = 13000,
        ftol = 1e-14,
        minimize_method = 'L-BFGS-B',
        ):
    """This function attempts to find a set of straight lines that corresponds 
    to a given arrangement of pseudolines, where each pair intersects at 
    distinct points specified in a table.

    For details on function parameters, refer to `test_and_find_lines()`.
    """

    return solver(copy.deepcopy(input_table), 
                  [],

                  rotational_symmetry = rotational_symmetry,
                  mirrored = mirrored,
                  
                  do_tests = False,
                  show_plots = show_plots,

                  ineq_epsilon = ineq_epsilon,
                  ineq_max = ineq_max,

                  min_angle = min_angle,
                  max_angle = max_angle,

                  main_coefficient = main_coefficient,
                  angles_coefficient = angles_coefficient,

                  maxiter = maxiter,
                  ftol = ftol,
                  minimize_method = minimize_method,
                  )