# Lecture 1: Linear-time string pattern matching

## Lecture outline

Linear-time approaches to exact pattern matching problem on strings

- Gusfield's _Z_-algorithm
- Boyer-Moore's algorithm
- Knuth-Morris-Pratt's algorithm

## Gusfield's _Z_-algorithm

- This is actually a linear-time algorithm to **preprocess** a given string.
- After preprocessing, the output from this algorithm (Zi-values) can be used to
  address a versatile set of problems that arise in strings.

### Defining Zi

For a string `str[1..n]`, define Zi (for each position `i > 1` in `str`) as the
**length** of the **longest substring _starting at_ position** `i` of `str` that
**matches its prefix** (i.e., `str[i...i+Zi-1] = str[1...Zi]`).

### Defining Zi-box

For a string `str[1..n]`, **and for any `i > 1` such that `Zi > 0`**, a Zi-box
is defined as the interval `[i...i+Zi-1]` of `str`.

### Defining ri

For a string `str[1..n]`, and for all `i > 1`, `ri` is the **right-most
endpoint** for all Z-boxes that begin at or before position `i`.

Alternately, `ri` is the largest value of `j + Zj - 1` over all `1 < j <= i`,
such that `Zj > 0`.
