# Lecture 7: B-Trees: A generalised balanced Search Tree

## What is covered in this lecture?

- A **generalisation** of the balanced search trees.
- **Standard operations** on B-trees (search, insert, delete)
- Space and time **complexity** issues.

## B-Trees

### Introduction

- B-tree **generalise balanced** search trees.
- By generalisation, the tree is **no longer** `binary` but has **many branches
  per node.**
- They are really powerful and are used on many mission critical systems that
  rely on a large amount of data stored on a **secondary storage** device
  (disk).
- Common examples are **very large databases** and **file-systems.**

### Properties

1. A `B-tree` is a **rooted tree**.
2. An arbitrary node looks like this:

   ![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8qeld0ylkj30sr06rq3h.jpg)

3. It has $n$ elements: $k_1 \le k_2 \cdots \le k_n$ that are stored in a
   **non-decreasing** (sorted) order.
4. It also stores $n+1$ **pointers/links to subtrees**:

   $T_1, T_2, \cdots, T_n, T_{n+1}$ that are **distributed regularly** between
   the elements.

5. Each successive $(k_i, T_i, T_{i+1}$ resembles a **fork**/node of a
   **binary** tree and has the BST **structural property**:
   $\{T_i\} \le k_i \le \{T_{i+1}\}$. Or, generalising

   $$\{T_1\} \le k_1 \le \{T_2\} \le k_2 \le \{T_3\} \le \cdots \le \{T_n\} \le k_n \le \{T_{n+1}\}$$

6. All leaves have the **same depth** (from the root).
7. **IMPORTANT**: The **number of elements per node** has a `lower bound` and an
   `upper bound`. These bounds are expresses using the parameter $t \ge 2$, also
   called the `minimum degree` of the B-tree:

   `Lower bound`: Each node must have **AT LEAST** $t$ **subtrees** as children
   or equivalently $t-1$ elements.

   - The only **exception** to this bound is for the root node.
   - A root node with 0 elements is an **empty** B-tree.
   - Root node with $\ge 1$ elements is a **non-empty** B-tree.

   `Upper Bound`: Every node must have **AT MOST** $2t$ subtrees (or
   equivalently $2t-1$ elements). A node of a B-tree is `full` if it reaches
   this bound.

The simplest B-tree is when $t=2$. Every internal node has either **2, 3, or 4
subtrees** connecting its **1, 2 or 3 elements**. This is specifically called a
`[2-3-4]` tree.

### Searching for element `x` in a B-tree

- Searching in B-tree is no different from searching in any `binary` search
  tree...
- However, since each node has $t \ge 2$ children, the decision is no longer
  `two-way` or `binary`.
- A **multi-way** branching decision has to be made according to its number of
  children/subtrees.

### Inserting into a B-tree

- Inserting into a B-tree is **slightly more** involved that inserting into a
  `binary` search tree (BST).
- As with a BST, we first search for a left position at which to insert the new
  key.
- However, with B-trees we simply cannot create a new leaf node and insert it,
  as it can **flout** the B-tree property.
- In B-trees, a new key is inserted into an **existing leaf node**.
  - However, this is only possible only if the left node is **NOT** full.
  - If the leaf node is **full**
    - The leaf node is `split` around its **median** element to form 2 nodes.
    - The median element **moves up** to the **parent node** of the original
      leaf node, to identify the dividing point of the two split nodes.
    - However, if the parent node is **full**, **split** the node to make room
      for the median to be pushed up (before insertion) into parent.
    - This implies, when traversing from root to leaf in a B-tree, **split** and
      **full parent node** of a sub(tree) along the insertion path.

### Deleting `x` from a B-tree

#### Case 1

If `x` belongs to a **leaf node** with $\ge t$ elements. Delete `x`.

#### Case 2

If `x` belongs to an **internal node**:

- If the left child node of `x` has a least $t$ elements, then find the
  `in-order predecessor` (say, `w`) in the left subtree, replace `x` with `w`,
  and then recursively delete `w` in the left subtree.
- Else if the right child node of `x` has at least $t$ elements, then find the
  `in-order successor` (say, `y`) in the right subtree, replace `x` with `y`,
  and the recursively delete `y` in the right subtree.
- Else, both `left` and `right` child nodes of `x` have **exactly** $t-1$
  elements, then **merge** `x` and child nodes, and recursively delete `x`.

#### Case 3

If the `traversal` is stopped because the 'appropriate' subtree containing `x`
has a node **exactly** $t-1$ elements, then:

- if this subtree's '`immediate sibling`' has **at least** $t$ elements, give an
  extra element to the appropriate subtree by `rotating` the predecessor or
  successor element **within the sibling node** to parent, followed by moving
  the original parent element to appropriate subtree.
- else, if its `immediate sibling` also has **exactly** $t-1$ elements, merge
  the parent element with both sibling elements to form a single node. They
  **may** reduce the height of the tree.

### Space and Time Complexities

#### Time Complexity

| Operation | Average Case   | Worst Case     |
| --------- | -------------- | -------------- |
| `search`  | $O(\log_t(n))$ | $O(\log_t(n))$ |
| `insert`  | $O(\log_t(n))$ | $O(\log_t(n))$ |
| `delete`  | $O(\log_t(n))$ | $O(\log_t(n))$ |

#### Space Complexity

|     | Average Case | Worst Case |
| --- | ------------ | ---------- |
|     | $O(n)$       | $O(n)$     |

## Summary

- B-trees are generalisations of balanced search trees.
- Designed to optimise access to secondary storage (e.g. hard disks).
- All leaf nodes are at the same height, so insertion and deletion
  $O(\log_t(n))$-time, all cases.
