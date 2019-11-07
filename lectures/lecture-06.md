# Lecture 6: Fibonacci Heaps

## Motivation for Fibonacci Heaps

- Improve run-time complexity of `Dijkstra's` shortest path algorithm.
- Similar to a `binomial heap`, a `Fibonacci heap` maintains a collection of
  (min-heap ordered) trees, however...
  - The trees in the collection are **less stringent** in their definitions,
    and..
    - ...while in a `binomial heap` **merging**/consolidation of trees is
      performed **eagerly** after each `extract-min` or `insert` option.
    - ... in a `Fibonacci heap` the consolidation/**merging** is performed
      **lazily**, by deferring until `extract-min` operation is next involved.

## Example of a Fibonacci heap

- A Fibonacci heap $H$ containing 5 trees, with total 14 elements.

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8pdjse61ej30sd08e75j.jpg)

- `H.min` is a pointer to root node (of a tree in the collection) with the
  minimum element.
- In a `Fibonacci heap`, each node/element is:
  - either `marked` (shown above as **black coloured nodes**)...
  - ...or `unmarked`/regular (shows as the grey coloured nodes above)

## Representation of a node in a Fibonacci heap

Each node `x`:

- stores a `key`, and has associated `payload` information;
- stores the number of its children: `x.degree`;
- stores of the node is marked or not: `x.mark`;
- has a pointer `x.parent` to its parent node;
- has a pointer `x.child` to **ANY ONE** of its children.
- `x` and its siblings form a **circular doubly linked list:**
  - So, `x` a pointer to its left sibling `x.left`...
  - ...and its right sibling `x.right`.

## Fibonacci heaps are represented using circular doubly linked lists

- Below is a visualisation of a circular doubly linked list representation (and
  other pointer) for the example shown above.

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8pdypeawjj30or0a7gne.jpg)

- This has several advantages:
  - This allows `insert` operations into any location in $O(1)$ time.
  - This allows `delete` operations from any location in $O(1)$ time.
  - This allows joining elements in one list to another in $O(1)$ time.

## Fibonacci Heaps - Attributes

Associated with each node/element $x$ in a Fibonacci heap $H$, is:

- The `number of children` in the child list:
  - We will call the `degree` of a node (`x.degree`).
- whether a node is marked or not - `x.mark`
  - '`marked`' implies the node has lost a child; `unmarked` implies it hasn't
    lost a child.
- Access to the Fibonacci heap $H$ is via the pointer to the `minimum` (key)
  element in the entire heap, denoted by `H.min`.
- Roots of all trees in the Fibonacci heap are connected by a `root_list`.
  - ...where each tree's root can be accesses via `left` and `right` pointers,
    starting from `H.min`.

## `insert` operation

`insert(x)` into a Fibonacci heap $H$.

- Access $H$ via pointer `H.min`.
- `insert(x)` into the `root_list`, making it the `left` sibling of `H.min`
  element/root.
- If $x <$ `H.min` (i.e., comparing their respective priorities/keys), update
  `H.min` to point to $x$ in teh root level.
- `insert(x)` is $O(1)$-time operation.

## `extract-min` operation

- Identify minimum element via the pointer `H.min`.
- To extract (and delete) minimum element
  - set the `current` pointer to the `right` sibling of `H.min`.
  - Promote/add all children (subtrees) to the `root_list`, and
  - **IMPORTANT**: Now run `consolidate` operation.

### `consolidate` operation

Fibonacci heaps run a `consolidate` operation only after a call to
`extract-min`.

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8peplq43jj30sr0ds0wb.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8pepza4spj30sr0fmgpk.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8peq9ybzjj30sr0fmwhn.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8peqivbuaj30sr0fmtcy.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8pequ6p6xj30sr0fmn1g.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8per54doaj30sr0id0xz.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8pere5u09j30sr0idgpf.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8permqgxxj30sr0idn0u.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8perunypwj30sr0id789.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8pes3wxuej30sr0imaed.jpg)

- `extract-min` operation (and `consolidation`) is now complete.
- Node: during the process of cycling through the `root_list` (during
  consolidation), we can keep track of the minimum root encountered, and update
  `H.min`.
- Run-time complexity is $O(\log(N))$ amortized.

## `decrease-key` operation

We want to decrease key of any node $x$ in a Fibonacci heap.

- This can be handled in two cases:
  - **case 1**: When this operation does not violate the heap property.
  - **case 2**: when it does.

### Case 1

When `decrease-key` does not violate the heap property. Simply decrease they key
on the node.

### Case 2a

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8pf2nd5bcj30sr0j3af0.jpg)

### Case 2b

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8pf32eoe7j30sr0j30xy.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8pf3ekki6j30sr0akq5l.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8pf3r6p1wj30sr09wq5p.jpg)

- Run-time complexity of `decrease-key` is $O(1)$ amortized.

## `Union` operation

`Union` operation involves combining two Fibonacci heaps, $H_1$ and $H_2$ into
one (used during `consolidation`):

- Takes $O(1)$ time.
  - This involves combining two root lists...
  - ...each represented by a circular doubly-linked lists,
  - ...and accessible via their respective minimum (root) elements, $H_1.min$
    and $H_2.min$...
  - ...before linking them into a single heap.

## `delete` operations

`delete` operation deletes some specified node $x$. This can be composed using
the following two operations:

- `decrease-key` of $x$ to $-\infty$
- `extract-min`

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
