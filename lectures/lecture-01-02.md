---
title: 'FIT3155 - Lectures 1 & 2'
subtitle: 'Linear-time string pattern matching'
---

# Lecture 1 & 2: Linear-time string pattern matching

## Outline

Linear-time pattern approaches to exact pattern matching problem on strings

- Gusfield's Z-algorithm
- Boyer-Moore's algorithm
- Knuth-Morris-Pratt's algorithm

## Gusfield's Z-algorithm

- This is actually a linear-time algorithm topre-processa given string.
- After pre-processing, the output from this algorithm ($Z_i$-values) can be
  used to address a versatile set of problems that arise in strings.

### Defining $z_i$

For a string `str[1..n]`, define $Z_i$ (for each position $i>1$ in `str`) as the
length of the longest substring starting at position $i$ of `str` that matches
its prefix (i.e., `str[i...i + Z_{i-1}] = str[1...Z_i]`).

### Defining $Z_i$-box

For a string `str[1..n]`, and for any $i>1$ such that $Z_i >0$, a $Z_i$-box is
defined as the interval `[i...i+Z_{i-1}]` of `str`.

### Defining $r_i$

For a string `str[1..n]`, and for all $i>1$, $r_i$ is the right-most endpoint
for all Z-boxes that begin at or before position $i$.

Alternately, $r_i$ is the largest value of $j + Z_{j-1}$ over all $1<j \le i$,
such that $Z_j>0$.

### Defining $l_i$

For a string `str[1..n]`, and for all $i>1$, $l_i$ is the left end of the Z-box
that ends at $r_i$.

- In the case there is more than on Z-box ending at $r_i$, then $l_i$ can be
  chosen to be the left end of any of those Z-boxes.

### Main point of Gusfield's Z-algorithm

- We have shown how to define $Z_i$, $Z_i$-box, $l_i$, $r_i$
- The fundamental pre-processing task of Gusfield's Z-algorithm relies on
  computing these values, given some string, in linear time.
- That is, for a string `str[1..n]`, we would like to compute $Z_i$, $Z_i$-box,
  $l_i$, $r_i$ for each position $i>1$ in `str` in $O(n)$-time.

### Overview of the linear-time pre-processing

- In this pre-processing phase, we compute $Z_i$, $Z_i$-box, $l_i$, $r_i$ values
  for each successive position $i$, starting from $i=2$.
- All successively computed $Z_i$ values are remembered.
  - Note: Each $Z_i$-box values can be computed from its corresponding $Z_i$
    value in $O(1)$ time.
- At each iteration, to compute $(l_i,r_i)$, this pre-processing only needs
  values of $(l_j,r_j)$ values are needed.
  - Note: no earlier $(l_j, r_j)$ values are needed…
  - …so, temporary variables $(l, r)$ can be used to keep track of the most
    recently computed $(l_{i-1},r_{r-1})$ values to update $(l_i,r_i)$.

### Base-Case

- To begin, compute $Z_2$ by explicit left-to-right comparision of characters
  `str[2..]` with `str[1..]` until a mismatch is found.
- if $Z_2>0$
  - Set $r$ (i.e., $r_2$) to $Z_2 + 1$
  - Set $l$ (i.e., $l_2$) to $2$
- else (i.e., if $Z_2 = 0$)
  - Set $r$ (i.e., $r_2$) to $0$
  - Set $l$ (i.e., $l_2$) to $0$

### Inductive assumption and general cases

Assume inductively…

- …we have correctly computed the values of $Z_2$ through to $Z_{k-1}$.
- ...that $r$ currently holds $r_{k-1}$,
- …that $l$ currently holds $l_{k-1}$.

For computing $Z_k$ at position $k$, these two scenarios arise:

- Case 1: If
- Case 2:Else

### Case 1:

- Compute $Z_k$ by explicitly comparing characters `str[k…q-1]` with
  `str[1…q-k]` until mismatch is found at some $q \ge k$.
- If $Z_k >0$:

  - Set $r$ (i.e.,$r_k$) to $q-1$
  - Set $l$ (i.e.,$l_k$) to $k$

- Otherwise they retain the same $l,r$ values as before.

### Case 2:

- The character `str[k]` lies in the substring `str[…r]` (i.e., within
  $Z_l$-box).
- By the definition of $Z_l$-box, `str[l…r]=str[1…Z_l]`.
- This implies the character `str[k]` is identical to `str[k-l+1]`.
- By extending this logic, it also implies that the substring `str[k…r]` is
  identical to `str[k-1+1…Zl]`.
- But, in previous iterations, we already have computed $Z_{k-l+1}$ value.

Case 2a, if $Z_{k-l+1}<r-k+1$:

- Set $Z_k$ to $Z_{k-l+1}$.
- $r$ and $l$ remain unchanged.

Case 2b, if $Z_{k-l+1}\ge r-k+1$:

- $Z_k$ must also be $\ge r-k+1$
- So, start explicitly comparing `str[r+1]` with `str[r-k+2]` and so on until
  mismatch occurs.
- Say the mismatch occurred at position $q \ge r + 1$, then:
  - Set $Z_k$ to $q-k$,
  - Set $r$ to $q - 1$.
  - Set $l$ to $k$.

### Pre-processing (of $Z_i$ values) for `str[1…n]` takes $O(n)$ time

- Total time is directly proportion to the SUM of:
  1. The number of iterations
  2. The number of character comparisons (**matches** or **mismatches**)
- This pre-processing has $n-1$ iterations.
- The number of **matches** and **mismatches** both at most $n$, because:
  - $r_k \ge r_{k-1}$ (for all iterations)
  - Update to $r_k$ is of the form $r_k=r_{k-1}+\delta$ (where $\delta \ge 0$).
  - But $r_k \le n$.
  - Thus, there are at most $n$ **matches** or **mismatches**.

### Using $Z$-algorithmfor linear-time exact pattern matching.

#### Recall the exact pattern matching problem

Given a reference text `txt[1…n]` and a pattern `pat[1…m]`, find **ALL**
occurrences, if any, of `pat` in `txt`.

#### Realising a linear-time solution using Gusfield's Z-algorithm/pre-processing

- Construct a new string by concatenation as follows:

  - `str = pat[1…m] + $ + txt[1…n]`.
  - Note, `|str| = m + 1 + n`.

- Pre-process $Z_i$ values corresponding to `str`, for $1<i \le m+n+1$.
- For any $i>m+1$, all $Z_i=m$ identifies an occurrence of `pat[1…m]` at
  position $i$ in `str`, and hence at position $i-(m+1)$ in `txt`. That is,
  $pat[1…m] = (str[1…i+m-1] \equiv txt[i-m+1…i-2])$.
- We already, showed that the computation of $Z_i$ values for any string `str`
  takes `O(|str|)` time).
- Thus, this pattern matching algorithm takes $O(m + n)$ time. `QED`

## Boyer-Moore Algorithm

Boyer-Moore algorithm incorporate three clever ideas:

1. Right-to-left scanning
2. Bad character shift rule
3. Good suffix shift rule

Caveat: An additional rule, termed in the field as the `Galil's optimisation`,
ensures linear runtime across all possible scenarios of `txt` and `pat`.

### Right-to-left scan

For any comparison ofpat[1..m]againsttxt[j…j+m-1], the Boyer-Moore algorithm
checks/scans for matched charactersrightto left (instead of the normal left to
right scan, as in the naïve algorithm).

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8f0nxxz92j30sg0b2jv6.jpg 'aaa')

So, after a mismatch during right-to-left scanning, to avoid naively shifting
`pat` rightwards by 1 position, BM algorithm employs two additional ideas/tricks
discussed below.

### Bad character shift rule

- Scanning right-to-left, we found a mismatch comparing `pat[3] = a` with
  `txt[5] = t`.
- But the right most occurrence in the entire `pat` of the mismatched character
  in `txt` (i.e. `txt[5]=t`) is at position 1 of `pat` (i.e., `pat[1]=t`).
- So, in this case, once case safely shift `pat` by **two places** to the right
  as to match characters `pat[1]=t` and `txt[5]=t` (instead of naively shifting
  by only one place).

#### Formalising 'Bad character' shift rule

- Let `pat[1..m]` and `txt[1..n]` be strings from the alphabet $N$.
- Pre-process `pat`, and store for each character $x \in N$, the rightmost
  position of occurrence of character $x$ in `pat`. _ Call this position,
  $R(x)$. _ Note, $R(x)=0$, when $x$ does not occur in `pat`.
- These pre-processed $R(x)$ values will be used (for > 1 position shifts of
  `pat` under `txt`, where possible).

Note: storing $R(x)$ values for `pat` requires at most $O(|N|)$ space, and one
lookup per mismatch.

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8f0v7j4ffj30sg070q4p.jpg)

- In some iteration of this algorithm, let's say `txt[j...j + m - 1]` and
  `pat[1...m]` are being compared via right-to-left scan.
- Let the kth character of `txt` counting from position $j$, i.e.
  $x = txt[j + k - 1]$, be **mismatched** with the kth character of the pattern
  `y = pat[k]`.
- **Shift/Jump RULE**: Then, the bad-character shift rule asks us to shift
  rightwards the `pat` along the `txt` by `max{1,k - R(x)}` positions.
- This implies, if `x` does not occur in `pat[1…m]` $(Rx=0)$, then the entire
  `pat` can be shifted one position past the point of **mismatch** in `txt`.

#### Extended Bad-Character Rule

When a **mismatch** occurs at some position $k$ in `pat[1…m]`, and the
corresponding **mismatched** character is `x = txt[j + k - 1]`, then **shift**
`pat[1..m]` to the right so that **the closest `x` in `pat` is to the left of
position $k$** is now below the (previously **mismatched**) `x` in `txt`.

- To achieve this, pre-process `pat[1…m]` so that, for each position in `pat`,
  and for each character $x \in N$, the position of the closest occurrence of
  $x$ to the left of each position can be efficiently looked up.
- A 2D (**shift/jump table**) of size $m \times |N|$ can store this information.

### Good Suffix Rule

- In some iteration, say `txt[j...j+m-1]` and are being compared via
  right-to-left scan.
- Let the kth character of `txt`, i.e., `x = txt[j+k-1]`, be mismatched with the
  kth chracter of the pattern `y = pat[k]`.
- If we knew that $p < m$ is the rightmost position in `pat` where the longest
  substring (of length $>=1$) ending at position $p$ matches its suffix, that
  is:
  - $pat[p-m+k+1…p] \equiv pat[k+1…m]$
  - $pat[p-m+k] \ne pat[k]$.
- Then, `pat` can be safely shifted right by $m-p$ positions,
- And a new iteration can be restarted.

#### Ideas to implement the 'good suffix' rule more efficiently

To efficiently implement the 'good suffix' rule, we take 'inspiration' from the
computation of $Z_i$ values in Gusfield's algorithm, and define $Z_i^{suffix}$
(specifically on `pat`) as follows:

Definition of $Z_i^{suffix}$:

Given a `pat[1…m]`, define $Z_i^{suffix}$ for (each position $i<m$) as the
**length** of the _longest substring **ending** at position_ $i$ of `pat` that
matches its **suffix** (i.e.,
$pat[i-Z_i^{suffix}+1…i] = pat[m-Z_i^{suffix}+1…m]$).

- Note, computation of $Z_i^{suffix}$ values on `pat` corresponds to the
  computation of $Z_i$ values on `reverse(pat)`.
- Thus, $Z_i^{suffix}$ values can be computed in $O(m)$ time for `pat[1…m]`.
- In fact, for each **suffix** starting at position $j$ in `pat`, we want to
  score the rightmost position $p$ in `pat` such that:
  - $pat[j..m] \equiv pat[p-Z_i^{suffix}+1..p]$
  - $pat[j-1] \ne pat[p-Z_i^{suffix}]$.

Store these rightmost positions as `goodsuffix(j) = p`. These can be computed
as:

```
m := |pat|
for j from 1 to m+1 do
  goodsuffix(j) :=0
endfor

for p from 1 to m-1 do
  j := m - Zˆ{suffix}_p + 1
  goodsuffix(j) := p
endfor
```

#### Using 'good suffix' rule during search

In any iteration, to use the '**good suffix**' rule, the following cases have to
handled:

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8ghvyag7qj30sg0be3zs.jpg)

Case 1a: if a mismatch occurs at some `pat[k]`, and `goodsuffix(k+1) > 0` then

- Shift `pat` by `m - goodsuffix(k+1)` places.

Case 1b: if a mismatch occurs at some `pat[k]`, and `goodsuffix(k+1 = 0)` then

- Shift `pat` by `m - matchedprefix(k+1)` places
  - `matchedprefix(k+1)` denotes the length of the **_largest_ suffix of**
    `pat[k+1..m]` that is identical to the **prefix of** `pat[1..m-k]`.
  - `matchedprefix(·)` values for `pat` can be precomputed using Z-algorithm in
    $O(m)$ time.

Case 2: when `pat[1...m]` fully matches `txt[j...j+m-1]`

- Shift `pat` by `m - matchedprefix(2)` places.

### Bringing all pieces together

Pre-processing step

- Pre-process `pat`…
  - … for jump tables (e.g. $(R(\cdot)$ values) needed for **'bad-character'**
    shifts
  - … for `goodsuffix(·)` and `matchedprefix(·)` and values needed for **'good
    suffix'** shifts.

Algorithm

- Starting with `pat[1..m]` vs. `txt[1..m]` , in each iteration, scan
  '**right-to-left**'.
- Use (extended) **bad-character** rule to find how many places to the right
  `pat` should be shifted under `txt`. Call this amount $n_{badcharacter}$.
- Use **good-suffix** rule to find how many places to the right `pat` should be
  shifted under `txt`. Call this amount $n_{goodsuffix}$.
- Shift `pat` to the right under `txt` by $max(n_{badcharacter},n_{goodsuffix})$
  places.

### Galil's optimisation to ensure linear runtime always

- Suppose, in some iteration, we are comparing `pat[1..m]` with
  `txt[j...j+m-1]`, via **right**-to-left scanning.
- Say `pat[k] != txt[j+k-1]` (or even say the entire `pat` matches in `txt`)…
- … in the next iteration (after applying some appropriate shift)…
- … if the left end of `pat[1]` lies between `txt[j+k-1...j+m-1]`…
- … then there is definitely a prefix `pat[1…]` that **matches**
  `txt[...j+m-1]`, which need not be explicitly compared, after this shift.
- Thus, in the next iteration, the right-to-left scanning can stop prematurely
  if position `txt[j+m-1]` is reached, to conclude there is an occurrence of
  `pat` in `txt`.
- Employing Galil's optimisation during shifting between iterations, the
  **Boyer-Moore algorithm** guarantees _worst-case time-complexity_ of $O(m+n)$.

## Knuth-Morris-Pratt (KMP) Algorithm

### Defining $SP_i$ values for `pat[1…m]`

Definition of $SP_i$:

Given a pattern `pat[1…m]`, define $SP_i$ (for each position $i$ in `pat`) as
the **length** of the **longest proper suffix** of `pat[1…i]` that **matches a
prefix** of `pat`, such that `pat[i+1] != pat[SPi+1]`.

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8gifnbft5j30sg06ljt1.jpg)

```
m := |pat|
for i from 1 to m do
  SP_i :=0
endfor

for j from m down to 2 do
  i := j + Z_j -1
  SP_i := Z_j
endfor
```

### KMP Algorithm overview

- KMP algorithm is described in terms of the $SP_i$ values.
- The general procedure/iteration of KMP involves:
  - Compare `pat[1...m]` against any region of `txt[j...j+m-1`] in the
    **natural** _left_-to-right direction.
  - In the first **mismatch**, while scanning **left**-to-right, occurs at pos
    $i+i$: that is, `pat[1…i] = txt[j…j+i-1]`
    - Shift `pat` to the right (relative to `txt`) so that …
    - `pat[1…SP_i]` is now aligned with `txt[j+i-SPi…j+i-1]`
    - **KMP shift rule** in other words, shift `pat` by exactly $i-SP_i$ places
      to the right.
  - Else, in the case of occurrence of `pat` is found in `txt` (i.e., no
    mismatch), then shift `pat` by $m-SP_m$ places.

## Summary

- Naïve algorithm takes $O(m * n)$-time
- Gusfield's Z-algorithm guaranteed in $O(n+m)$-time, worst case.
- Boyer-Moore's algorithm takes
  - $O(n+m)$-time worst case …
  - … but $O(\frac{m}{n})$-time (sublinear) in most 'realworld' usage.
- Knuth-Morris-Pratt algorithm also takes $O(n+m)$-time worst-case, but inferior
  in performance to Boyer-Moore in practice.
