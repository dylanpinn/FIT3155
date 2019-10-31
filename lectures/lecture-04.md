---
title: 'FIT3155 - Lecture 4'
subtitle: 'The disjoint-set data structre'
---

# Lecture 4: The disjoint-set data structure

## Equivalence relationship

- A `relation` $\bigotimes$ is defined over members/elements of some set $S$.
- For any pair of elements $(a,b)$ from this set $S$.
  - $a \bigotimes b$ results in a `true` or `false` answer.

What is an equivalence relation

An **equivalence relation** is a relation $\bigotimes$ that satisfies:

- reflexive property: $a \bigotimes a$ for all $a$ in set $S$.
- symmetric property: $a \bigotimes b$ implies $b \bigotimes a$ for all $a,b$ in
  $S$.
- transitive property: $a \bigotimes b$ and $b \bigotimes c$ implies
  $a \bigotimes c$ for all $a,b,c$ in $S$.

## Equivalence class

- An **equivalence class** of an element $a \in S$ defines a **subset** of
  elements from $S$, where all elements in that subset are **related** to $a$.
- Every element of $S$ belongs to exactly one equivalence class (subset).
- To check if two elements $a$ and $b$ are related, we only have to check if
  they are in the same equivalence class.

## Basic disjoint-set data structure

Disjoint-set data structure supports two basic operations:

- `find(a)`: This returns the name/label of the subset (i.e. equivalence class)
  containing the element $a$ in the set $S$.
  - Note: the name/label of the subset itself is **arbitrary**.
  - All that really matters is this: For two elements $a$ and $b$ to be related,
    we should check if `find(a) == find(b)`.
- `union(a,b)`: Merge the two (disjoint) subsets containing $a$ and $b$ in $S$.
  - In practice this is implemented as `union(find(a), find(b))`

The input to this data structure is initially a collection of $N$ elements, that
are treated to be disjoint (no relation) with each other. Using `find(·)` and
`union(·,·)` operations, the relations are dynamically checked and (new
relations) established.

## Some applications of Disjoint set data structure

- Kruskal's algorithm
- Keeping track of connected components of a graph
- Computing Lowest Common Ancestor in trees
- Checking equivalence of finite state automata
- Hindley-Milner polymorphic type inference
- etc.

### Recall

- Kruskal's algorithm introduced a basic implementation of disjoint-set data
  structure.
- This involved maintaining the disjoint data-structure using:
  - an **array of linked-lists** to support `union(a,b)`
  - a **membership array** to support `find(a)`
- Using the implementation above:
  - `find(a)` operation can be achieved via array access in $O(1)$-time.
  - `union(a,b)` operation can be achieved in $O(N)$-time, because it requires:
    - appending two linked lists (each denoting a subset being merged)
    - change **membership** array for elements in the **smaller** of the two
      subsets, so that they are now merged.

## New disjoint set data structure using just an array

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8gjln8alcj30sl079aax.jpg)

- The above example shows $N=8$ disjoint elements initially.
- These are numbered `{0,1,2,...,7}`.
- A simple `parent array` is used to capture this information.
- In the `parent array`, the imaginary parent is denoted as -1.
- In general, each element in the array points to its parent.

### Example: Data structure after a series of `union(.)` operations

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8gkjkz5axj30sl0ekmym.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8gkjts5uej30sl0ekjsw.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8gkk5jz0yj30sl0fzdhi.jpg)

## Smart Union algorithms - Motivation

- `union(·)` in the earlier examples performed a union by making the second
  tree/subset a subtree of the first.
- This was an arbitrary choice.
- In general, a smarter way would to make the **smaller** tree (in terms of the
  number of elements in it) the subtree of the larger tree. This is called
  `union-by-size`.
- An even smarter approach would be to make the **shorter**/shallower tree (in
  tree height) the subtree of the **taller**/deeper tree. This is called
  `union-by-height`.

## `Union-by-size`

When `union(a,b)` is carried out using `union-by-size`:

- Ensure $a$ and $b$ are in two disjoint trees.
- Then point the root node of the tree with **smaller number of elements** to
  the root for the larger one.
  - If both sizes are equal, break the tie arbitrarily.
- The cell corresponding to the merged root in the `parent array` is updated to
  store the merged tree/subset size (as a **negative number**).

### `Union-by-size` example

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8h2no5b82j30sl0fz402.jpg)

![image-20191031112205526](https://tva1.sinaimg.cn/large/006y8mN6ly1g8h2nyu0fhj30sl0h7dhj.jpg)

![image-20191031112220361](https://tva1.sinaimg.cn/large/006y8mN6ly1g8h2o83xa4j30sl0h7dhl.jpg)

![image-20191031112243400](https://tva1.sinaimg.cn/large/006y8mN6ly1g8h2ombui5j30sl0i1dhp.jpg)

![image-20191031112254176](https://tva1.sinaimg.cn/large/006y8mN6ly1g8h2ot7bhjj30sl0i1dhq.jpg)

### Implementation of `Union-by-size`

#### Initialization

- At the start, initialise $N$ **disjoint subsets** of elements.
- This involves initialising the `parent array` to all -1 values.
- Recall: In `union-by-size`, the cell in the `parent array` corresponding to
  any (disjoint) tree's root node, stores the `size of the tree` as a
  `negative number`.

```c
InitSet(N) {
  for  (a = 0 to N-1) {
    Make_disjoint_set(a)
  }
}

Make_disjoint_set(x) {
  parent[x] = -1
}
```

#### `find(a)`

Search until the `root` of the tree (containing $'a'$) is reached; return the
root's label/index.

```c

find(a) {
  // find root of the tree containing 'a'
  while (parent[a] >= 0) { // note: while parent[a] not negative
    a = parent[a]
  }
  return a  // 'a' now includes the root node of the subtree/subet
}
```

#### `union(a,b)`

When executing `union(a,b)`, ensure $a$ and $b$ are in two disjoint trees. Then
link the root node of the smaller **bold** (in size) tree to the root for the
larger one. If both sizes are equal, break the tie `arbitrarily`. Update the
merged tree size (stored as a negative number).

```c
union(a,b) {
  root_a = find(a) // find root of tree containing 'a'
  root_b = find(b) // find root of tree containing 'b'

  if (root_a == root_b) return // 'a' and 'b' in the same tree

  size_a = -parent[root_a]
  size_b = -parent[root_b]

  if (size_a > size_b) {
    parent[root_b] = root_a // link smaller tree's root to larger
    parent[root_a] = -(size_a + size_b)
  } else { // if (size_b >= size_a)
    parent[root_a] = root_b
    parent[root_b] = -(size_a + size_b)
  }
}
```

## `Union-by-height` (and `union-by-rank`)

When `union(a,b)` is carried out using `union-by-height`:

- Ensure $a$ and $b$ are in disjoint trees.
- Then make the disjoint tree with `shorter height` a subtree of the taller
  tree.
- That is, make the root of the shorter tree point to the root of the taller
  one, after union.
  - If both heights are equal, break the tie arbitrarily.
- The cell corresponding to the merged root in the `parent array` is updated to
  store the merged tree's (`height + 1`) as a **negative number**.

`Union-by-rank` is **essentially identical** to `union-by-height`, but includes
an additional optimisation called `path compression` to be discussed later..

### Example

- Initial State

  ![image-20191031114316618](https://tva1.sinaimg.cn/large/006y8mN6ly1g8h3a0fxblj30sl07mgmh.jpg)

- `union(4,5)`

  ![image-20191031114331690](https://tva1.sinaimg.cn/large/006y8mN6ly1g8h3a9qjvkj30sl09mwfi.jpg)

- `union(6,7)`

  ![image-20191031114342703](https://tva1.sinaimg.cn/large/006y8mN6ly1g8h3agsqdrj30sl09mt9s.jpg)

- `union(5,7)`

  ![image-20191031114406682](https://tva1.sinaimg.cn/large/006y8mN6ly1g8h3avvt73j30sl0bvmyf.jpg)

- `union(3,7)`

  ![image-20191031114422918](https://tva1.sinaimg.cn/large/006y8mN6ly1g8h3b5nrdzj30sl0bvdh4.jpg)

### Implementation of `Union-by-height`

#### Initialization

In union by height/rank, the cell in the `parent array` corresponding tot eh
root element of any disjoint tree/set, **now** stores the `height of the tree`
coded as a negative number.

```c
InitiSet(N) {
  for (a = 0 to N-1) {
    Make_disjoint_set(a)
  }
}

Make_disjoint_set(x) {
  parent[x] = -1
}
```

#### `find(a)`

Same implementation as for `union-by-size`.

#### `union(a,b)`

When executing `union(a,b)`, ensure $a$ and $b$ are in two disjoint trees. Then
link the root node of the shorter (in `height`) tree to the root of the taller
tree. If both heights are equal, break the tie arbitrarily.

```c
union(a,b) {
  root_a = find(a) // find root of tree containing 'a'
  root_b = find(b) // find root of tree containing 'b'

  if (root_a == root_b) return // 'a' and 'b' in the same tree

  height_a = -parent[root_a] // height of tree containing 'a'
  height_b = -parent[root_b] // height of tree containing 'b'

  if (height_a > height_b) {
    parent[root_b] = root_a // link shorter tree's root to taller
  } else if (height_b > height_a) {
    parent[root_a] = root_b
  } else { // if (height_a == height_b)
    parent[root_a] = root_b
    parent[root_b] = -(height_b + 1) // update to height
  }
}
```

### `Union-by-rank` is same as `Union-by-height` but with an additional optimisation implemented during `find(·)`

- Union-by-height with a with a simple optimisation during `find(·)` operation
  yields `union-by-rank`.
- Has a drastic impact on the `amortized` complexity of the disjoint-set data
  structure.

#### Amortized Complexity

Amortized analysis attempts to track the complexity of performing a
`sequence of operations` on a particular data structure, rather than analysis
just the worst-case complexity of a single operation.

#### Path compression during `find(·)` operation in `union-by-rank`

##### Path compression

When executing `find(a)`, every node along the path from the `'root'` node to
$'a'$ has its **parent index changed to point `directly` to the root.**

Notes:

- Path compression is performed during `find(·)` operation.
- It is independent of the strategy used for `union(·,·)` operation.

#### Path Compression illustration

Consider this example.

Before `path compression`

![image-20191031120008687](https://tva1.sinaimg.cn/large/006y8mN6ly1g8h3rk7g63j30no06l40c.jpg)

Say we are running `find(14)` on the above state. The resultant path compressed
tree will be:

![image-20191031120053887](https://tva1.sinaimg.cn/large/006y8mN6ly1g8h3scbhpdj30no07m0us.jpg)

#### Path compression based on `find(a)` implementation

After finding the root of the tree containing $'a'$, change the parent pointer
of all nodes along the path to point directly to the root.

```c
find(a) {
  // find root of the tree containing 'a'
  if (parent[a] < 0) { // root is reached
    return a
  } else {
    return parent[a] = find(parent[a])
  }
}
```

## Complexity Analysis

Complexity analysis of Disjoint set data structure using union-by-size,
union-by-height and union-by-rank.

### Analysis of `union-by-size`

#### Lemma

For **any** disjoint-set tree constructed using `union-by-size` with a root node
$\textcircled{r}$, with its size being `size`$(\textcircled{r})$ and its height
being `height`$(\textcircled{r})$, we have the following statement:

$$
\mathtt{size}(\textcircled{r}) \ge 2^{\mathtt{height}(\textcircled{r})}
$$

#### Proof by Induction\

`Base case:` When $\textcircled{r}$ is the root of a tree containing just one
node (i.e., itself):

$$\mathtt{size}(\textcircled{r}) = 1$$ $$\mathtt{height}(\textcircled{r}) = 0$$

Substituting these values into the statement of the Lemma, the base case is
true.

`Inductive case:`

- Assume the statement is true for all disjoint-trees in the data structure
  after a sequence of $k$ `union(·,·)` operations.
- In the $(k + 1)$-th `union(·)`, let us say we are merging two disjoint trees,
  one rooted at $\textcircled{s}$ and other rooted at $\textcircled{r}$.
- Without loss of generality, let
  $\mathtt{size}(\textcircled{r}) \ge \mathtt{size}(\textcircled{s})$

Case 1: $\mathtt{height}(\textcircled{r}) > \mathtt{height}(\textcircled{s})$

\begin{align*} \text{After } (k + 1)\text{-th merge: } \text{ new }
\mathtt{size} &\ge \text{ old } \mathtt{size}(\textcircled{r}) \\ &\ge
2^{\text{old} \mathtt{height}(\textcircled{r})} \quad (\text{inductive step})\\
\text{But 'new } \mathtt{height}'(\textcircled{r}) = '\text{old }
\mathtt{height}(\textcircled{r})' \\ \implies \text{new }
\mathtt{size}(\textcircled{r}) &\ge 2^{\text{new }
\mathtt{height}(\textcircled{r})} \end{align*}

This proves the lemma for this case.

Case 2: $\mathtt{height}(\textcircled{r}) \le \mathtt{height}(\textcircled{s})$

\begin{align*} \text{After } (k + 1)\text{-th merge: } \text{ new }
\mathtt{size} &= \text{ old } \mathtt{size}(\textcircled{r}) +
\mathtt{size}(\textcircled{s}) \\ &\ge s \times
\mathtt{size}(\textcircled{s})\quad(\because \mathtt{size}(\textcircled{r}) \ge
\mathtt{size}(\textcircled{s})) \\ &\ge 2 \times
2^{\mathtt{height}(\textcircled{s})} \quad (\text{inductive step})\\ &\ge
2^{\mathtt{height}(\textcircled{s}) + 1} = 2^{\mathtt{height}(\textcircled{r})}
\end{align*}

This proves the lemma. $\quad \quad \blacksquare$

#### Corollary

For a disjoint set with $N$ elements, both `find(·)` and `union(·,·)` take
worst-case $O(\log_{2}(N))$ effort.

#### Proof

\begin{align*} \mathtt{size}(\textcircled{r}) &\ge
2^{\mathtt{height}(\textcircled{r})} \\ \text{But }
\mathtt{size}(\textcircled{r}) \text{ is bounded above by } N \\ \implies N &\ge
2^{\mathtt{height}(\textcircled{r})} \\ \implies \log\_{2}N &\ge
\mathtt{height}(\textcircled{r}) \end{align*}

- `find(·)` in the worst case takes
  $O(\mathtt{height}(\textcircled{r})), \implies O(\log_{2}N$ effort.
- `union(·,·)` involves 2 `find(·)` operations + $O(1)$ effort,
  $\implies \log_2(N)$ effort.

$\blacksquare$

### `union-by-height` analysis is same as `union-by-rank` analysis, ignoring `path compression`

Recall that `union-by-rank` and `union-by-height` are essentially the same,
especially when there is **NO** path compression applied in `find(·)` operation.

In the remaining notes, `rank` of any node $\textcircled{x}$ is same as its
`height` (i.e., maximum number of hops needed from the leaf nodes to reach
$\textcircled{x}$).

### `Union-by-rank` analysis (w/o `path compression`)

#### Observation 1

For any $\textcircled{x}$ that is **NOT** the root node, we have:

$$\mathtt{rank}(\textcircled{x}) < \mathtt{rank}(\text{parent}(\textcircled{x}))$$

#### Observation 2

For any element $\textcircled{x}$ that is **NOT** the root node,
$\mathtt{rank}(\textcircled{x})$ remains unchanged in all further/future
operations.

#### Observation 3

For any path up from $\textcircled{x}$ to its root node $\textcircled{r}$
$$\textcircled{x} \rightarrow \textcircled{w} \rightarrow \textcircled{v} \rightarrow \textcircled{u} \cdots \textcircled{r}$$
that observed ranks from a strictly increasing sequence
$$\mathtt{rank}(\textcircled{x}) < \mathtt{rank}(\textcircled{w}) < \mathtt{rank}(\textcircled{v}) < \mathtt{rank}(\textcircled{u}) < \cdots < \mathtt{rank}(\textcircled{r})$$

#### Lemma

Any node $\textcircled{x}$ with $\mathtt{rank}(\textcircled{x}) = k$, we have:

$$\mathtt{size}(\textcircled{x}) \ge 2^k$$

#### Proof\

`Base case`: When the tree contains only a singleton node $\textcircled{x}$,
then $\mathtt{rank}(x) = 0$ and $\mathtt{size}(x) = 1$.

Thus, the statement is true for the base case.

`Inductive case`:

- Assume that the statement is true for all nodes up to rank $=k-1$
- A node of rank $=k$ can only be created when merging 2 subtrees with roots of
  rank $=k-1$ each.
- Inductively, each rank $=k-1$ subtree has $\ge 2^{k-1}$ nodes.
- $\implies$ the new size of the tree $\ge 2 \times 2^{k-1} = 2^k$

Thus, the statement is also true for the general case.
$\quad \quad \blacksquare$

#### Corollary

From observations above and Lemma
$$\mathtt{height}(\textcircled{x}) \le \log_2(N)$$ where $N$ is the total number
of elements in the disjoint set being merged under union-be-height/union-by-rank
(w/o path compression) operations.

From this it can be shown that:

- `find(·)` in the worst case takes
  $O(\mathtt{height}(\textcircled{r})), \implies O(\log_2N)$ effort.
- `union(·,·)` involves 2 `find(·)` operations + $O(1)$ effort,
  $\implies log_2(N)$ effort.
