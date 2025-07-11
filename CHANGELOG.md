# Changelog

All significant modifications to this project will be recorded in this file. The structure follows the guidelines of [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.5.0] - 2025-07-08

### Added

- Fish-eye projection for `draw_lines()`.

## [1.4.0] - 2025-06-18

### Added

- Function that adds a line between 1 and 2 to an odd table (`add_1_2_line`)
- Function that reverses the order of lines (`reverse_order`)
- New optimal arrangements (`n=23`, `n=27`)

## [1.3.0] - 2024-11-07

### Added

- Generate bigger maximal arrangements from the existing one using `gen_2nm1` and `gen_2nm1_repeat`
- Optimal arrangements for `n=29` and `n=33` in the [Kobon Gallery](https://zegalur.github.io/line-order/gallery/kobon.html)

## [1.2.0] - 2024-11-01

### Added

- Parallel lines support
- Support of multi-line cross-points for `find_lines()` and `draw_lines()`
- New gallery

## [1.1.0] - 2024-10-29

### Added

- Renumbering and reordering of a table (`reindex_table()`)
- Solving in the form `y=mi(x-ai)` for Proposition 3.1. from [this paper](https://www.researchgate.net/publication/1893173_On_simple_arrangements_of_lines_and_pseudo-lines_in_P2_and_R2_with_the_maximum_number_of_triangles).
- Second [gallery](https://zegalur.github.io/line-order/gallery/index_2.html)

## [1.0.0] - 2024-10-21

### Added

- A working version of the tool
- A brief description in README.md
- An auto-generated showcase gallery

