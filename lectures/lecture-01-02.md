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
its prefix (i.e., `str[i...i + Z_{i−1}] = str[1...Z_i]`).

### Defining $Z_i$-box

For a string `str[1..n]`, and for any $i>1$ such that $Z_i >0$, a $Z_i$-box is
defined as the interval `[i...i+Z_{i−1}]` of `str`.

### Defining $r_i$

For a string `str[1..n]`, and for all $i>1$, $r_i$ is the right-most endpoint
for all Z-boxes that begin at or before position $i$.

Alternately, $r_i$ is the largest value of $j + Z_{j−1}$ over all $1<j \le i$,
such that $Z_j>0$.

### Defining $l_i$

For a string `str[1..n]`, and for all $i>1$, $l_i$ is the left end of the Z-box
that ends at $r_i$.

- In the case there is more than on Z-box ending at $r_i$, then $l_i$ can be
  chosen to be the left end of any of those Z-boxes.

### Main point of Gusfield's Z-algorithm

- We have shown how to define $Z_i$, $Z_i$−box, $l_i$, $r_i$
- The fundamental pre-processing task of Gusfield's Z-algorithm relies on
  computing these values, given some string, in linear time.
- That is, for a string `str[1..n]`, we would like to compute $Z_i$, $Z_i$−box,
  $l_i$, $r_i$ for each position $i>1$ in `str` in $O(n)$-time.

### Overview of the linear-time pre-processing

- In this pre-processing phase, we compute $Z_i$, $Z_i$−box, $l_i$, $r_i$ values
  for each successive position $i$, starting from $i=2$.
- All successively computed $Z_i$ values are remembered.
  - Note: Each $Z_i$−box values can be computed from its corresponding $Z_i$
    value in $O(1)$ time.
- At each iteration, to compute $(l_i,r_i)$, this pre-processing only needs
  values of $(l_j,r_j)$ values are needed.
  - Note: no earlier $(l_j, r_j)$ values are needed…
  - …so, temporary variables $(l, r)$ can be used to keep track of the most
    recently computed $(l_{i−1},r_{r−1})$ values to update $(l_i,r_i)$.

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

- …we have correctly computed the values of $Z_2$ through to $Z_{k−1}$.
- ...that $r$ currently holds $r_{k−1}$,
- …that $l$ currently holds $l_{k−1}$.

For computing $Z_k$ at position $k$, these two scenarios arise:

- Case 1: If
- Case 2:Else

### Case 1:

- Compute $Z_k$ by explicitly comparing characters `str[k…q−1]` with
  `str[1…q−k]` until mismatch is found at some $q≥k$.
- If $Z_k >0$:

  - Set $r$ (i.e.,$r_k$) to $q−1$
  - Set $l$ (i.e.,$l_k$) to $k$

- Otherwise they retain the same $l,r$ values as before.

### Case 2:

- The character `str[k]` lies in the substring `str[…r]` (i.e., within
  $Z_l$−box).
- By the definition of $Z_l$−box, `str[l…r]=str[1…Z_l]`.
- This implies the character `str[k]` is identical to `str[k−l+1]`.
- By extending this logic, it also implies that the substring `str[k…r]` is
  identical to `str[k−1+1…Zl]`.
- But, in previous iterations, we already have computed $Z_{k−l+1}$ value.

Case 2a, if $Z_{k−l+1}<r−k+1$:

- Set $Z_k$ to $Z_{k−l+1}$.
- $r$ and $l$ remain unchanged.

Case 2b, if $Z_{k−l+1}≥r−k+1$:

- $Z_k$ must also be $≥r−k+1$
- So, start explicitly comparing `str[r+1]` with `str[r−k+2]` and so on until
  mismatch occurs.
- Say the mismatch occurred at position $q \ge r + 1$, then:
  - Set $Z_k$ to $q−k$,
  - Set $r$ to $q - 1$.
  - Set $l$ to $k$.

### Pre-processing (of $Z_i$ values) for `str[1…n]` takes $O(n)$ time

- Total time is directly proportion to the SUM of:
  1. The number of iterations
  2. The number of character comparisons (**matches** or **mismatches**)
- This pre-processing has $n-1$ iterations.
- The number of **matches** and **mismatches** both at most $n$, because:
  - $r_k≥r_{k−1}$ (for all iterations)
  - Update to $r_k$ is of the form $r_k=r_{k−1}+𝛿$ (where $𝛿≥0$).
  - But $r_k≤n$.
  - Thus, there are at most $n$ **matches** or **mismatches**.

### Using $Z$−algorithmfor linear-time exact pattern matching.

#### Recall the exact pattern matching problem

Given a reference text `txt[1…n]` and a pattern `pat[1…m]`, find **ALL**
occurrences, if any, of `pat` in `txt`.

#### Realising a linear-time solution using Gusfield's Z−algorithm/pre-processing

- Construct a new string by concatenation as follows:

  - `str = pat[1…m] + $ + txt[1…n]`.
  - Note, `|str| = m + 1 + n`.

- Pre-process $Z_i$ values corresponding to `str`, for $1<i≤m+n+1$.
- For any $i>m+1$, all $Z_i=m$ identifies an occurrence of `pat[1…m]` at
  position $i$ in `str`, and hence at position $i−(m+1)$ in `txt`. That is,
  $pat[1…m] = (str[1…i+m−1] ≡ txt[i−m+1…i−2])$.
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

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8f0nxxz92j30sg0b2jv6.jpg)

So, after a mismatch during right-to-left scanning, to avoid naively shifting
`pat` rightwards by 1 position, BM algorithm employs two additional ideas/tricks
discussed below.

### Bad character shift rule

- Scanning right-to-left, we found a mismatch comparing `pat[3] ≡ a` with
  `txt[5] ≡ t`.
- But the right most occurrence in the entire `pat` of the mismatched character
  in `txt` (i.e. `txt[5]≡t`) is at position 1 of `pat` (i.e., `pat[1]≡t`).
- So, in this case, once case safely shift `pat` by **two places** to the right
  as to match characters `pat[1]≡t` and `txt[5]≡t` (instead of naively shifting
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
  rightwards the `pat` along the `txt` by `max{1,k − R(x)}` positions.
- This implies, if `x` does not occur in `pat[1…m]` $(Rx=0)$, then the entire
  `pat` can be shifted one position past the point of **mismatch** in `txt`.

#### Extended Bad-Character Rule

When a **mismatch** occurs at some position $k$ in `pat[1…m]`, and the
corresponding **mismatched** character is `x = txt[j + k - 1]`, then **shift**
`pat[1..m]` to the right so that **the closest `x` in `pat` is to the left of
position $k$** is now below the (previously **mismatched**) `x` in `txt`.

TODO: FINISH FROM HERE

- To achieve this, pre-processpat[1…m]so that, for each position inpat, and for
  each character , the position of the closest occurrence of to the left of each
  position can be efficiently looked up.
- A 2D (shift/jump table)of size can store this information.

### Good Suffix Rule

- In some iteration, say and are being compared via right-to-left scan.
- Let thekth character oftxt, i.e.x=txt[j+k−1], be mismatched with thekth
  chracter of the patterny=patk.
- If we knew that is the rightmost position inpatwhere the longest substring (of
  length ending at position matches its suffix, that is:

      * patp−m+k+1…p≡patk+1…m
      * patp−m+k≠pat[k].

- Then,patcan be safely shifted right by positions,
- And a new iteration can be restarted.

patp−m+k+1…p≡patk+1…m

#### Ideas to implement the 'good suffix' rule more efficiently

To efficiently implement the 'good suffix' rule, we take 'inspiration' from the
computation ofZivalues in Gusfield's algorithm, and defineZisuffix(specifically
onpat) as follows:

Definition ofZisuffix:Givenapat[1…m],defineZisuffixfor (each positioni<m) as
thelengthof thelongest substring ending at positioniofpatthat matches
itssuffix(i.e.,pati−Zisuffix+1…i=pat[m−Zisuffix+1…m]).

- Note, computation ofZisuffixvalues onpatcorresponds to the computation
  ofZivalues onreverse(pat).
- Thus,Zisuffixvalues can be computed inO(m)time forpat[1…m]. In fact, for
  eachsuffixstarting at position inpat, we want to score the rightmost position
  inpatsuch that:

patj..m≡patp−Zisuffix+1..p\* patj..m≡patp−Zisuffix+1..p

- patj−1≠pat[p−Zisuffix]. Store these rightmost positions asgoodsuffixj=p.These
  can be computed as:

m := |pat|

forjfrom1to m+1do

goodsuffix(j) :=0

endfor

forpfrom1to m-1do

j := m - Zˆ{suffix}\_p +1

goodsuffix(j) := p

endfor

#### Using 'good suffix' rule during search

In any iteration, to use the 'good suffix' rule, the following cases have to
handled:

![la:
1
txt
pat
Case
1
goodsuffix(k+l) > O
mismatched
characters
x
goodsuffix(k+l) = p
m ](@attachment/c83b7580-53e1-4d7e-a226-4ba26b5b54d5.png)
Case 1a:if a mismatch occurs at some ,and then

- Shiftpatby places. Case 1b:if a mismatch occurs at somepat[k],
  andgoodsuffixk+1=0then

- Shiftpatby places

      * matchedprefix(k+1)denotes the length of thelargest suffix ofpat[k+1..m]that is identical to theprefix ofpat1..m−k.
      * matchedprefix(.)values forpatcan be precomputed using Z-algorithm inO(m)time.

Case 2:when fully matches

- Shiftpatby places.

### Bringing all pieces together

Pre-processing step

- Pre-processpat…

      * … for jump tables (e.g.

  values) needed for 'bad-character' shifts \* … for and values needed for 'good
  suffix' shifts.

Algorithm

- Starting with vs. , in each iteration, scan'right-to-left'.
- Use (extended)bad-characterrule to find how many places to the rightpatshould
  be shifted undertxt. Call this amountnbadcharacter.
- Usegood-suffixrule to find how many places to the rightpatshould be shifted
  undertxt. Call this amountngoodsuffix.
- Shiftpatto the right undertxtbymax⁡(nbadcharacter,ngoodsuffix)places.

### Galil's optimisation to ensure linear runtime always

- Suppose, in some iteration, we are comparing with , viaright-to-leftscanning.
- Saypatk≠txt[j+k−1](or even say the entirepatmatches intxt)…
- … in the next iteration (after applying some appropriate shift)…
- … if the left end ofpat[1]lies between …
- … then there is definitely a prefixpat[1…]thatmatches , which need not be
  explicitly compared, after this shift.
- Thus, in the next iteration, the right-to-left scanning can stop prematurely
  if positiontxt[j+m−1]is reached, to conclude there tis an occurrence
  ofpatintxt.
- Employing Galil's optimisation during shifting between iterations, the
  Boyer-Moore algorithm guaranteesworst-case time-complexityof .

## Knuth-Morris-Pratt (KMP) Algorithm

### DefiningSPivalues forpat[1…m]

Definition ofSPi: Given a patternpat[1…m], defineSPi(for each positioniinpat) as
thelengthof thelongest proper suffixofpat[1…i]thatmatches a prefixofpat, such
thatpati+1≠pat[SPi+1].

![Example
1 2 3 4 5 6 7 8 9 19 11 12
Pat= b b c ca e b bc abd
O SPF 1 SPF O
SPI
SPI ](@attachment/bd11c284-3671-49f6-936f-c48c101b2e57.png)m
:= |pat|

forifrom1to mdo

SP_i :=0

endfor

forjfromm down to2do

i := j + Z_j -1

SP_i := Z_j

endfor

### KMP Algorithm overview

- KMP algorithm is described in terms of theSPivalues.
- The general procedure/iteration of KMP involves:

      * Compare

  against any region of in thenaturalleft-to-right direction. \* In the
  firstmismatch, while scanning left-to-right, occurs at posi+i: that
  is,pat1…i≡txt[j…j+i−1]

          * Shiftpatto the right (relative totxt) so that …
          * pat1…SPiis now aligned withtxt[j+i−SPi…j+i−1]
          * KMPshift rulein other words, shiftpatby exactlyi−SPiplaces to the right.

      * Else, in the case of occurrence ofpatis found intxt(i.e., no mismatch), then shiftpatbym−SPmplaces.

## Summary

- Naïve algorithm takes -time
- Gusfield's Z-algorithm guaranteed in -time, worst case.
- Boyer-Moore's algorithm takes

  - O(n+m)-time worst case …
  - … butO(mn)-time (sublinear) in most 'realworld' usage.

- Knuth-Morris-Pratt algorithm also takes -time worst-case, but inferior in
  performance to Boyer-Moore in practice.
