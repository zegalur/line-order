from .utils import reindex_table
from copy import deepcopy


def gen_2nm1(table_in):
    """This function returns a new arrangement of `(2n-1)` pseudo-lines based
    on an existing arrangement of `n` pseudo-lines by completing a first line 
    with a network of inter-crossing `(n-1)` lines.

    Returns a dictionary:
        `status` - Status of the operation (`OK` or `ERROR: [...]`).
        `table` - Resulting table.
    """

    N = len(table_in)

    # Check if arrangement is supported.

    for row in table_in:
        for cross_point in row:
            if type(cross_point) is list:
                return { 'status' : 'ERROR: Multi-line cross-points are not '
                                  + 'yet supported.' }
    if (N % 2) == 0:
        return {'status':'ERROR: Only the odd number of lines is supported now.'}
    if N < 3:
        return {'status':'ERROR: To few lines. At least 3 lines is required.'}
    for row in table_in:
        if len(row) != (N-1):
            return { 'status' : 'ERROR: Parallel lines are not yet supported.' }
    
    # Reindex the input table so that the first line become the last line.
    table = reindex_table(table_in, 2)

    # Complete the last line with a cascade of inter-crossing lines.

    template = deepcopy(table[N-1])

    # Copy last row (N-1) times.
    for i in range(N-1):
        table.append(deepcopy(template))

    # The current order of all new lines, including the last line.
    order = list(range(N))

    cursors = [0] * N
    top = template[0] < template[1]

    for i in range(N):
        i0 = 0 if top else 1
        for j in range((N-1) // 2):
            i1 = i0 + 2*j
            i2 = i0 + 2*j + 1
            l1 = order[i1] + N - 1
            l2 = order[i2] + N - 1
            table[l1].insert(cursors[order[i1]], order[i2] + N)
            table[l2].insert(cursors[order[i2]], order[i1] + N)
            cursors[order[i1]] += 1
            cursors[order[i2]] += 1
            order[i1], order[i2] = order[i2], order[i1]
        for j in range(N):
            cursors[j] += 1
        if i != (N-1):
            line = template[i] - 1
            index = table[line].index(N)
            table[line].pop(index)
            for (k, l) in enumerate(order):
                table[line].insert(index + k, l + N)
        top = not top

    res = {
        'status' : 'OK',
        'table' : reindex_table(table, N + ((N-1)//2)),
    }

    return res


def gen_2nm1_repeat(table_in, count=1):
    """Uses `gen_2nm1()` repeatedly to make bigger and bigger arrangements."""
    res = { 'status' : 'OK', 'table' : deepcopy(table_in) }
    for i in range(count):
        res = gen_2nm1(res['table'])
        if res['status'] != 'OK':
            break
    return res