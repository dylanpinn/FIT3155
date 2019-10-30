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
- A simple **parent array** is used to capture this information.
- In the **parent array**, the imaginary parent is denoted as -1.
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
- The cell corresponding to the merged root in the **parent array** is updated
  to store the merged tree/subset size (as a **negative number**).
