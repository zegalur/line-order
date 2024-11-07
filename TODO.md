# LineOrder

LineOrder TODO list.

### Todo

- [ ] Add: check input data for consistency (e.g., if N % S == 0).
- [ ] Add: n=19 arrangements to the gallery.
- [ ] Add: n=20 arrangements to the gallery.
- [ ] Fix: incorrect solutions for arrangements with parallel lines and rotational symmetry (e.g. incorrect 3-rotational symmetry solution for kobon-18)

### In Progress

- [ ] Add: support for cross-points with 3 and more lines.
    - [x] Format: `6:[1,2,[3,4],5]` where `[3,4]` means line 6 crosses lines 3 and 4 at the same cross-point.
    - [ ] Add: multi-line cross-points support for `draw_pseudolines()`.
    - [ ] Add: multi-line cross-points support for `reindex_table()`.

### Done ✓

- [x] Add: Renumbering and reordering of a table.
- [x] Fix: `sqrt` value error in `draw_lines.py` when the line is outside the circle.
- [x] Fix: `linalg` error in `get_intersection_point()` when lines are parallel.
- [x] Add: find arrangements with `y = mi(x - ai), ai=tan(..)` conditions.
- [x] Add: generate pseudo-line arrangements using a process similar to Proposition 3.1.

