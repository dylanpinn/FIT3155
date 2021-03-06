---
title: 'FIT3155 - Lecture 3'
subtitle: 'Linear time suffix tree construction'
---

# Lecture 3: Linear time suffix tree construction

## What is covered in this lecture?

Linear-time suffix tree construction

- Ukkonen algorithm (suffix tree construction)

## Introduction

The substring (matching) problem

Given a reference text `txt[1...n]`, preprocess `txt` such that any given
pattern `pat[1...m]` can be searched in linear time proportional to the length
of the pattern, $O(m)$.

- Suffix trees (and similarly suffix arrays) permit solving the above (and many
  other related) problems. They are very versatile.
- Suffix trees unravel the composition of any string, and permit efficient
  access to them.

## String definitions

Given

- A `prefix` of `str[1..n]` is a **substring** `str[1..j]`,
  $\forall 1 \le j \le n$.
- A `suffix` of `str[1..n]` is a **substring** `str[i..n]`,
  $\forall 1 \le i \le n$.
- A `substring` of `str[1..n]` is any `str[j..i]`,
  $\forall 1 \le j \le i \le n$.
- Therefore,
  - A substring is a **prefix of a suffix**
  - (or equivalently) a substring is a **suffix of a prefix**

## Efficient Suffix Tree Construction using `Ukkonen's` algorithm

### Recall from FIT2004:

### Path compressed suffix tries = suffix trees

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8ez9n35jfj30uw0n476q.jpg){width=75%}

### Efficient representation of suffix trees requires $O(n)$ space

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8ez9y88r8j30uw0g6tan.jpg){width=75%}

Note, instead of storing the edge labels as substrings **explicitly**, we can
store them **implicitly** using$(j,i)$ denoting the substring `str[j..i]`, where
$1 \le j \le i \le n$.

### Building a suffix treenaively

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8ezalk9nvj30uw0a2402.jpg)

1. Start with the (empty) root node of the suffix tree $r$
2. Insert suffix **1** (`str[1...]1`) into an empty tree.
   - Call the resultant tree $T_1$
3. Insert suffix **2** into $T_1$
   - Note `str[2...]` is not a prefix of `str[1...]`
   - So create a new leaf node for `str[2..]` suffix, branching off at $r$.
   - Call the resultant tree $T_2$
4. Insert suffix **3** into $T_2$
   - Note `str[3..]` is not a prefix of `str[1...]` or `str[2...]`.
   - So create a new leaf node for `str[3]` suffix, again branching of at $r$
   - Call the resultant tree $T_3$
5. Insert suffix **4** into $T_3$
   - Note `str[4..5]` is the longest common prefix shared with the suffix
     `str[1...]`.
   - So, a new node $u$ is inserted
     - Along the edge between $r$ and the leaf node **1**
     - With another edge branching off $u$ to the new leaf node **4**.
   - Call the resultant tree $T_4$
6. Insert suffix **5** into $T_4$
   - Note `str[5..5]` is the longest common prefix shared with the suffix
     `str[2..]`.
   - So a new node $v$ is inserted
     - Along the edge between $r$ and the leaf node **2**
     - With another edge branching out from $v$ to the new leaf node **5**
   - Call the resultant tree $T_5$
7. Insert suffix **6** into $T_5$
   - Note the suffix `str[6..6]` denotes the sepecial terminal character `$`
   - This creates a new isolated edge branching off the root $r$.

![Completed tree](https://tva1.sinaimg.cn/large/006y8mN6ly1g8ezavv7d4j30jh0ajq4h.jpg){
width=75% }

### Ukkonen's linear-time algorithm -- introduction

Ukkonen's algorithm uses the following main ideas:

1. Construct and use an '`implicit suffix tree`' data structure
   - The actual suffix tree is computed after iteratively constructing (over
     many phases) an implicit suffix tree.
2. Enhance this `implicit suffix tree` using '`suffix links`'.
   - This helps make the traversals on the implicit tree much faster.
3. Gain from a set of implementational '**tricks**':
   - These tricks avoid unnecessary computations, thus speeding up the algorithm
     drastically.

### Implicit suffix trees

The relationship between an implicit suffix tree and its regular suffix tree can
be understood by the following operations on the regular suffix tree:

- Start with a regular suffix tree (of `str = a b c a b`).
- Remove all terminal (`$`) characters in the regular suffix tree.
- Then, remove all edges without edge labels (i.e. substrings)
- Then, path compress the tree by removing all nodes that do not have at least
  two children.

![Regular vs Implicit](https://tva1.sinaimg.cn/large/006y8mN6ly1g8ezbj4ac1j30r10jcdk2.jpg)

### Ukkonen's algorithm builds implicit suffix trees incrementally in `phases`

Given a string `str[1..n]`, Ukkonen's algorithm proceeds over $n$ "`phases`"

- Each `phase` $i+1$ (where $1 \le i+1 \le n$) builds the `implict` suffix tree
  (denoted by `implicitST`$_{i+1}$) for the **prefix** `str[1..i+1]`.
- Importantly, each `implicitST`${_i+1}$ is incrementally computed using the
  `implicitST`$_i$ from the previous phase.
  - The construction of `implicitST`$_{i+1}$ from `implicitST`$_i$, in turn
    involves several `suffix extension` steps, one for each suffix of the form
    `str[j..i+1]`, where $j=1…i+1$ in that order.

### Each phase involves suffix extensions

- In any phase $i+1$, the suffixes in `implicitST`$_i$ (from the previous phase
  $i$) undergo `suffix extensions` to accommondate the **additional character**
  , `str[i+1]`.
- Thus, extending any suffix $j$, where $1 <= j <= i + 1$, in the current phase
  $i+1$ involves:
  - Finding the path from the root node $r$ corresponding to the suffix
    `str[j...i]`, and
  - Extending `str[j..i]` by appending `str[i+1]` to the suffix.

### Algorithm at a very high level

```
Construct implicitST1
For i from 1 to n-1
  Begin PHASSE i + 1
    For j from 1 to i + 1
      Begin SUFFIX EXTENSION j
      - Find end of path from root denoting str[j..i] in the
        current state of the suffix tree.
      - Apply one of the three suffix extension rules.
    End of extension step j
  End of phase i + 1 (implicitSTi+1 computed)
```

### Suffix extension rules

#### Rule 1 of 3

If the path `str[j..i]` in `implicitST`$_i$ **ends at a leaf**, adjust the
**label of the edge** to that leaft to account for the added character
`str[i+1]`.

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8ezbylquwj30sg0egmzk.jpg)

#### Rule 2 of 3

If the path `str[j..i]` in `implicitST`$_i$ **does NOT** end at a leaf, and the
next chracter in the existing path is some $x \ne$ `str[i+1]`, then split the
ege after `str[..i]` and create a new node $u$, followed by a new leaf numbered
$j$; assign character `str[i+1]` as the edge label betwene the new node $u$ and
leaf $j$.

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8ezcae6f9j30sg0dhjtv.jpg)

#### Rule 2 of 3 - an alternative scenario that can arise

If the path `str[j..i]` in `implicitST`$_i$ **does NOT** end at a leaf, and the
next chracter in the existing path is some $x \ne$ `str[i+1]`, **and `str[i]`
and $x$ are separated by an existing node $u$** ,then split the ege after
`str[..i]` and create a new node $u$, followed by a new leaf numbered $j$;
assign character `str[i+1]` as the edge label betwene the new node $u$ and leaf
$j$.

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8ezclrg2vj30sg0dhgnv.jpg)

#### Rule 3 of 3

If the path `str[j..i]` in `implicitST`$_i$ **does NOT** end at a leaf, but is
within some edge label, and the next character in that path is `str[i+1]`, then
`str[i+1]` is already in the tree. **No further action needed**.

![Rule 3](https://tva1.sinaimg.cn/large/006y8mN6ly1g8ezcvmgykj30gv0iugmv.jpg){width=50%}

#### Example\

![Example](https://tva1.sinaimg.cn/large/006y8mN6ly1g8ezd5axzsj30sg0jgn5a.jpg){width=75%}

### Speeding up tree traversal usingsuffix links

Suffix links are simply `pointers` between internal nodes of an (implicit)
suffix tree, that speed up traversal time in each phase.

#### Definition of a suffix link

- Let $u$ and $v$ be two internal nodes of an implicit suffix tree.
- Let the traversal from root node $r$ to $u$ yield some substring
  `str[j..k-1]`.
- Let the traversal from root node $r$ to $v$ yield a substring `str[j+1..k-1]`.
- Then the pointer from $u$ to $v$ defines a suffix link between those nodes.

#### Example\

![Example](https://tva1.sinaimg.cn/large/006y8mN6ly1g8ezdev4xcj30sg0jgju3.jpg){width=75%}

### KEY OBSERVATION:

Every internal node of an implicit suffix tree has a suffix link **from** it.

- If, in some suffix extension $j$ of phase $i+1$, a new internal node $u$ is
  added to the current state of the implict suffix tree.
  - i.e., rule **2** of the suffix extension rules is applicable here.
- This means before $u$ is added, the path `str[j..i]` is continued by a
  character (say $x$), where $x \ne$ `str[i+1]`.
- This implies, in the next suffix extension $j+1$ of the same phase $i+1$:
  - **Either** the path `str[j+1..i]` continues **ONLY VIA** character $x$.
    - Which implies, a **new** internal node $v$ must be added, after
      `str[j+1..i]`, that brances to the new leaf $j+1$ via character `str[i+1]`
  - **Or** the path `str[j+1..i]` already ends in an **existing** internal node
    $v$
    - With one branch below extending via character $x$
    - And one (or more) branch(es), via character(s) $\ne$ `str[i+1]`
  - Thus, new suffix link $u$ to $v$ **WILL BE created** in $j+1$ extension.

### Following the trail of suffix links to build `implicitST`$_{i+1}$ from `implicitST`$_i$

Recall that in the extension $j$ of phase $i+1$ the algorithm locates suffix
`str[j..i]`, and extends it by `str[i+1]`, for each $j$ increasing from 1 to
$i+1$. Suffix links are used to speed these extensions.

#### Extension 1, phase

- This first suffix represents the full prefix `str[1..i+1]` considered in this
  phase.
- We have to locate first the suffix `str[1..i]`.
- Note, suffix `str[1..i]` is the longest string represented in the implict
  suffix `implicitST`$_i$ (from which `implicitST`$_{i + 1}$ is being computed).
- Let `ptr` be a pointer to the leaf containing `str[1..i]` in `implicitST`$_i$.
- Given `ptr`, the extension from to `str[1..i]` can be handled in constant
  time.

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8ezdrjxk4j30cv0h2q3w.jpg){width=50%}

#### Extension 2, phase

- Consider the edge ending at leaf 1 (after extension 1).
- Let $u$ be the internal node forming the edge with leaf 1.
- Let the substring corresponding to that edge be `str[k..i+1]`.
- In this extension, to find `str[2..i]` (and extend to `str[2..i+1]`):
  - Walk up EXACTLY ONE EDGE from leaf 1 to $u$.
  - From $u$, follows its suffix link to $v$.
  - From $v$, walk down along the path `str[k..i]`
  - Then apply the pertinent suffix extension rule, by walking down fromvand
    then appending `str[i+1]`.

### General extension procedure for phase

For any extension $j \ge 2$ of phase $i+1$ repeats the same general idea

1. Find the first node $u$ **AT OR ABOVE** the end of `str[j-1..i]`.
   - i.e., backtracking **AT MOST one edge** from the end of `str[j-1..i]`.
   - Let the substring `str[k..i]` (possibily empty) denote the edge label
     between $u$ and end of `str[j-1..i]`.
2. If $u \ne r$, traverse the suffix link from $u$ to $v$. Walk down from $v$
   along the path dictated by the substring `str[k..i]`.
   - On the other hand, if $u=r$, then no choice but to naively follow traverse
     the path from from $r$.
3. Once at the desired point (i.e., end of `str[j..i]`), apply pertinent suffix
   extension rules.
4. Repeat items 1-3 above until each suffix `str[j..i+1]` (of the prefix
   `str[1..i+1]`), for $1 \le j \le \le i+1$ is `implicitST`$_{i+1}$.
5. During these extensions, any new internal nodeucreated in extension $j-1$,
   gets its suffix link to it corresponding node $v$ in the next extension $j$.

## Implementational trick 1 - skip/count trick

In item 2 (above), during extension $j$, the extension requires you to walk down
form node $v$, along the path `str[k..i]`. Instead of a character-by-character
comparision while walking down from $v$, one could speed up the traversal by
skipping over the nodes below $v$, while keeping track of the total substring
length skipped along the path until the right location is reached.

- Let `str[k..i] = z a b c d e f h h y`
- From node $v$, ask how many characters representing the edge starting with
  $z...$. Here 2.
- Since $10 > 2$, skip to the node receiving that edge.
- In `str[k..i]`, the 3rd $(3 = 2+1)$ character is $b$.
- Again, ask how many characters representing the edge starting with `b...`
  Again it is 2.
- Since $10 > 2 + 2$, skip to the node receiving the edge.
- From `str[k..i]`, the 5th $(5 = 2+2+1)$ chracter is d.
- Again, ask how many characters representing the edge starting with `d...`. It
  is 3.
- Since $10 > 2 + 2 + 3$, skip to the node receieving that edge.
- ... and so on until the node beyond which furhter skips are not
  possible/necessary.

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8eze0dz8mj308u0ddab2.jpg){width=50%}

## Implementational trick 2 - space-efficient representation of edge-labels/substrings

Recall, given any string `str[1..n]`, any substring can be represented by just
two numbers: (`start-index`, `end-index`). Thus, the entire Ukkonen algorithm is
processed using this space efficient ($O(n)$-space) representation.

Below is an implicit suffix tree of the string `str=a a b b a a b b`, using
(`start-index`, `end-index`) edge label representation.

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8eze6e9bfj30n009vq57.jpg){width=50%}

## Implementational trick 3 - premature extension stopping criterion: `Showstopper’ rule!`

In any phase $i+j$, if `rule 3` extension applies in some suffix extension $j$,
then extensions $j+1, j+2, \dots i+1$ will all use `rule 3` because:

- when `rule 3` is used with extension $j$, implies the path corresponding to
  `str[j..i]` continues wiht the character `str[i+1]`.
- This implies, the path corresponsding to the substring `str[j+1..i]` also
  continues with the character `str[i+1]`.
- Similarly, this remains true for all subsequent extensions.
- **Punchline**: Since `rule 3` requires `no further action`, extensions in
  phase can `STOP` prematurely on encountering `rule 3`, and the algorithm can
  directly start the extensions for the next phase.

## Implementational trick 4 - rapid leaf extension trick

### Observation - In Ukkeonen’s algorithm, **once a leaf, always a leaf**

If at some phase $i$ in Unkkonen’s algorithm, a leaf is created and labelled $j$
(denoting a suffix `str[j..i]` of the prefix `str[1..i]`), then that leaf will
remain a leaf in all subsequent phases ($> i$).

### Why?

- Leaf node, when created (via `rule 2`) always stores as its label, the
  starting index $j$ denoting where the corresponding suffix starts.
- In subsequent phases, **whenever** this suffix is extended at the leaf (via
  `rule 1`), only the edge-label connecting the leaf gets updated, and **_not_
  the leaf node label**.
- Phase 1 consists of a single edge tree, root node $r$ to leaf node numbered 1
  (created using rule 2).
- In each phase $i$, suffixes get extended (using rule 1) and (potentially) new
  suffixes get added (using rule 2)
  - before the phase ends (either prematurely using rule 3, or naturally when
    $j$ reaches $i$).
- Let `last`i $_{j_{i}}$ denote the **last** extension $j$ (via rule 1 or 2) for
  phase $i$.
- Since the number of leaves between two consecutive phases is non-decreasing
  - and the new leaf is created only upon application of rule 2, it follows that
    `last`i $_{j_{i}} \le$ `last`i $_{j_{i+1}}$
- Note: if for any suffix extension $j$ in phase $i$ we applied rule 1 or rule
  2, it automatically implies that the suffix extension $j$ in phase $i+1$ will
  require (only) rule 1.
- Therefore, after each phase $i$, the observation that `last`i $_{j_{i}} \le$
  `last`i $_{j_{i+1}}$ can be exploited and we can omit/avoid **explicit**
  suffix extensions 1 to last `last`i $_{j_{i}}$ for the **next** phase $i+1$,
  and do so rapidly using the (implicit) extension trick shown below.
- From the space-efficient representation we know that any edge is represented
  using two numbers: (`start-index`, `end-index`).
- For each edge connecting the `leaf node` (whose index is $j$, in phase $i+1$,
  the edge label would be of the form $(k,i+1)$, denoting the substring
  `str[k..i+1]`).
- In each suffix extension, instead of EXPLICITYLY updating the `end-index` (of
  the edge to the leaves) to $i+1$, index it IMPLICITLY to a `global-end`
  variable, i.e., (`k, global-end`)
  - Note: when phase $i+1$ starts, `global_end` si implicitly $i+1$.
- In phase $i+1$, since rule 1 applies to all extensions of leaf nodes froim 1
  to `last`i $_{j_{i}}$
  - **no additional explicit work** is required to implement extensions
    $j=1,j=2,\dots j = \text{last}_{j_{i}}$. These can be straightaway ignored.
- EXPLICIT extensions only start from $j = \text{last}_{j_{i}} + 1$ until the
  first extension using rule 3 or until phase ends.

## Putting trick 4 pieces together - procedure to handle extensions in any single phase

Summarising trick 4, for any phase $i+1$, the extension procedure is as follows

1. Increment `gloabal_end` index to $i+1$.
   1. With just this operation, suffix extensions 1 to `last`$_{j_{i}}$ are
      implicitly complete without any additional work.
2. Explicitly compute successive extensions starting from $j = $
   `last`$_{j_{i}} + 1$, until some position $p \le i + 1$ where the phase
   either prematiruely terminates (after first encountering rule 3 extension),
   or all extensions are completed for this phase.
3. To prepare for the next phase $i + 2$, set `last`$_j{_{i+1}}$ to $p-1$ and
   repeat the procedure above, until all phases are complete.

### Observation

Two consecutive phases share **at most** one index $p$ where an EXPLICIT
extension is executed.

## Creating the final suffix tree from `implicitST`$_n$ for `str[1..n]`

The final suffix tree from its implicit version can be computed in $O(n)$-time
as follows:

- First add a string terminal symbol `$` to the end of `str`, i.e. `str[i..n]$`.
- Continue one more phase on `implicitST`$_n$ to account for this new character.
- The effect is that no suffix is now a prefix in `implictST`$_n$.
- So each suffix of `str[1..n]` gets appended by `$`, yielding the
  `regular/explicit` suffix tree.

## Ukkonen’s algorithm runs in $O(n)$ time for a stirng `str[1..n]`

- There are only $n$ phases in the algorithm
- Each phase stares at most 1 explicit suffix extension
- Hence, total number of explicit suffix extensions is at most $2n$.
- To quantify the effor in each extension:
  - If the node in the tree capturing `str[j-1..i]` is at depth $d$ from $r$
  - Then $u$ is at depth at most $d-1$.
  - This implies the node receiving its suffix link, $v$ is at most $d-2$.
- Total number of skips over **all phases** is $O(n)$
- From this, it follows, Ukkonen takes $O(n)$-time.
