# LineOrder

LineOrder TODO list.

### Todo

- [ ] Add: check input data for consistency (e.g., if N % S == 0).

### In Progress

- [ ] Add: support for cross-points with 3 and more lines.
    - [ ] Format: `6:[1,2,[3,4],5]` where `[3,4]` means line 6 crosses lines 3 and 4 at the same cross-point.
- [ ] Add: support for parallel lines.
    - [ ] Format: `[[2],[1,3],[2]]` means line 1 and 3 are parallel (because 3 isn't in the first row and 1 isn't in the third row).

### Done ✓

- [x] Add: Renumbering and reordering of a table.
- [x] Fix: `sqrt` value error in `draw_lines.py` when the line is outside the circle.
- [x] Fix: `linalg` error in `get_intersection_point()` when lines are parallel.
- [x] Add: find arrangements with `y = mi(x - ai), ai=tan(..)` conditions.

