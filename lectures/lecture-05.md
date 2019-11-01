# Lecture 5: Binomial heap and its amortised analysis

## Priority queues (implemented using heaps)

Recall that the heap data structure was used in several applications:

- Heap sort
- Dijkstra's shortest path algorithm
- Prim's algorithm

Heaps support the following operations:

- `insert` a new element (containing key w/ payload) into a heap.
- identify the `min` element in an existing heap
- `extract-min` (identify and delete min) element in an existing heap
- `decrease-key` of an element in an existing heap.

## Mergeable Heaps

Binomial Heaps and Fibonacci heaps support (at least) the following operations:

`insert`

: inserts a new element into the existing heap

`min`

: finds the min element in heap

`extract-min`

: finds and deletes the min element in the heap

`merge`

: merges two heaps into one

`decrease key`

: decreases the elements key

`delete`

: removes an element form the heap

## Binomial `tree`

Binomial trees are defined recursively:

- The binomial tree of order 0 (or $B_0$ in short) is a single node tree.
- The binomial tree of order 1 ($B_1$) is created from two $B_0$ trees, by
  making one $B_0$ tree the child of the other.
- The binomial tree of order 2 ($B_2$) is created from two $B_1$ trees, by
  making one $B_1$ tree the child of the other.
- and so on...

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8hlsa0qxgj30eg0fjq4l.jpg){width=50%}

### Properties of a Binomial `tree`

Any binomial tree of order $k$ has the following properties:

- The number of nodes in any $B_k$ is $2^k$.
- The height of any $B_k$ is $k$.
- The root node of any $B_k$ tree has $k$ subtrees as children.
- Deleting the root node of $B_k$ (with its edges/links) yields $k$ independent
  lower order binomial trees $B_{k-1},B_{k-2},\ldots,B_0$

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8hlveew7rj30sb0bzac1.jpg)

### Why are these trees called `binomial`

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8hlw5gym9j30sb09r40i.jpg)

#### Main property

A main property of any $B_k$ tree is that the `number of nodes` at any given
depth $d$ is given by the `binomial coefficient` ${k}\choose{d}$.

## What is a binomial `heap`

A binomial `heap` is a forest (i.e., a set) of binomial `trees` such that:

- **each** binomial tree in the set satisfies the heap property - i.e., **each**
  tree-node's key is $\le$ its children's keys.
- There is `at most` one (i.e., either 0 or 1) binomial tree of a given order in
  that set.

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8hm0bf5ioj30sb0bvjt5.jpg)

### How to find which order trees are there in a Binomial heap?

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8hm1hzaraj30sb09vgmh.jpg)

For the above binomial `heap`:

- $N = 19$.
- (Minimal) Binary representation of 19 gives: `1 0 0 1 1`
- The 1's above are at bit positions 0, 1 and 4.
- Therefore, the binomial `heap` with $N = 19$ contains 3 binomial `trees`:
  $B_0, B_1, B_4$ trees.

### Binomial heap properties

For any binomial `heap` containing $N$ elements, the following properties hold:

- There are at most $\lfloor \log_2N \rfloor + 1$ binomial `trees`.
- The height of each binomial `tree` is $\le \lfloor \log_2N \rfloor$.
- The 1's in the **minimal binary representation** of $N$ tells us which
  order/degree binomial `trees` form the binomial `heap` of $N$ elements.
- The element with the `minimum` key in the entire heap will be one of the root
  nodes of the `trees` in the collection.

## Representing a binomial heap

- Unlike **binary** heaps, `binomial` heaps are stored explicitly using a `tree`
  data structure.
- Each node $x$:
  - is denoted by a `key`, and has associated `payload` information.
  - has a pointer `parent[x]` to its parent node.
  - has a pointer `child[x]` to its **leftmost** child node
    - if node $x$ has zero children, then `child[x] = nil`
  - has a pointer `sibling[x]` to the immediate **sibling** of $x$ to its right.
    - if node $x$ is the rightmost child of its parent, then `sibling[x] = nil`
  - stores `degree[x]` which is the number of children of $x$ (i.e., same as the
    `order` of the binomial tree rooted at $x$)
- Finally, the roots of the binomial trees within a binomial heap are organised
  in a linked list, referred to as the `root list`.

### Binomial heap data structure representation - example

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8hmug8ru9j30r80gjjt9.jpg)

## Operations on a Binomial Heap

### Merging two binomial `trees` into one

First merging two binomial `trees`, each of the `same` order (say) $k$ results
in an order $k+1$ binomial tree, where:

- the two roots are linked, such that...
- ...the root containing the `larger` **key** becomes the `child` of the root
  with `smaller` **key**.

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8hmwsj0r0j30s507w75g.jpg)

- With merging two binomial `trees` established, we can now define `merging` of
  two binomial `heaps` (each containing a collection of trees).
- Heaps are merged in a way that is `reminiscent` of how we add two numbers in
  binary:

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8hmyba6isj30s507wt9b.jpg)

#### Example of merging 2 binomial heaps containing 19 and 7 elements each\

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8hmza20wkj30nt0ffn0d.jpg)

### Complexity of `merge` between 2 binomial heaps containing $N$ elements

Running time is $O(\log N)$ worst-case:

- time is bounded by maximum number of binomial `tree` merges.
- the number of `trees` in each heap with $N$ elements is bounded by
  $\lfloor \log N \rfloor + 1$
- Thus, merging two heaps with $N$ elements, in worst case, requires
  $\lfloor \log N \rfloor + 1$ number of tree merges.

### `extract-min`

This is used to identify and delete the minimum element among all `root nodes`
of the trees in the heap.

- Identify the `min` node among the nodes in the root level of th heap, and
  delete it.
- We know that deleting the root node of any $B_k$ tree yields:
  $B_{k-1}, B_{k-2},\ldots,B_0$.
- Then, progressively `merge` the binomial trees of the same order (starting
  from order 0) until the binomial heap definition is satisfied.

#### Running time of `extract-min` operation

- Running time is $O(\log N)$ worst-case
  - effort required to find the `min` is $O\log N$.
  - effort required to promote (to root level) and merge subtrees formed upon
    deletion of the min element is $O(\log N)$.
  - Total effort: $O(\log N)$

### `decrease-key`

We want to decrease key of any node $x$ in a binomial heap containing $N$
elements.

- decrease key of node $k$.
- if min-heap property is violated (i.e., $x < \mathtt{parent[x]}$), bubble up
  node $x$.
- Running time (worst-case): $O(\log N)$ - depth of the binomial tree in which
  $x$ resides is bounded above by $\lfloor \log N \rfloor$.

### `delete`

We want to delete any node $x$ is a binomial heap containing $N$ elements.

- run `decrease-key` by setting $x$ to $- \inf$.
- run `extract-min`.
- Running time (worst-case): $O(\log N)$.

### `insert`

We want to insert a new element $x$ into an existing binomial heap $H_1$

- Make a new binomial heap $H_2$ with $x$ as its **only** element.
- Run $\mathtt{merge}(H_1,H_2)$.

#### Amortized analysis of `insert` operation

Consider the problem of building a `binomial` heap of $N$ elements:

Claim

: A `binomial` heap of $N$ elements can be built by $N$ successive insert in
$O(N$)-time.

- Time required for inserting **each** element $x$ into a heap $H_1$ (starting
  from an empty heap) involves:
  - time to create a new binomial heap $H_2$ containing only 1 element $x$ -
    which requires constant effort, `plus`
  - time to merge $H_2$ into $H_1$.
- Total over $N$ insertions requires:
  - $O(N)$ + total merging time

It is easy to see (by beholding how the numbers starting from 0 change when 1 is
added each time):

- The **first insertion** into an empty $H_1$ heap requires **zero** merges.
- The second insertion involves exactly **one** merge between to $B_0$ binomial
  trees, yielding a heap containing one $B_1$ tree.
- The **third insertion** involves **zero** merges
  - $H_1$ before insertion contains 2 elements (contained in 1 $B_1$ tree).
  - merging the new inserted element into $H_1$ adds only a new $B_0$ tree to
    the existing $B_1$ tree. Therefore no merges.
- The fourth insertion involves exactly **two** merges.
- the **fifth insertion** involves **zero** merges
- $\vdots$

When inserting $N$ elements, if the binary representation of number elements in
$H_1$ before each insertion ends in:

- `......0`, the effort takes only 1 unit of time.
- `.....01`, the effort takes only 2 units of time.
- `....011`, the effort takes only 3 units of time.
- `...0111`, the effort takes only 4 units of time.
- `..01111`, the effort takes only 5 units of time.

##### Total time over $N$ insertions

- $T = \frac{N}{2} \times 1 + \frac{N}{4} \times 3 \ldots \le 2N$
- Such a series is called an **Arithmetico-Geometric series.**

Thus total time is bounded by $O(N)$, implying that each `insert` into a
binomial heap is $O(1)$ amortised.

## Summary

| Opertation            | Binary heap | Binomial heap |
| --------------------- | ----------- | ------------- |
| `make-new-heap`       | $O(1)$      | $O(1)$        |
| `min`                 | $O(1)$      | $O(\log N)$   |
| `extract-min`         | $O(\log N)$ | $O(\log N)$   |
| `merge`               | $O(N)$      | $O(\log N)$   |
| `decrease-key`        | $O(\log N)$ | $O(\log N)$   |
| `delete`              | $O(\log N)$ | $O(\log N)$   |
| `insert` - worst-case | $O(\log N)$ | $O(\log N)$   |
| `insert` - amortised  | $O(1)$      | $O(1)$        |
