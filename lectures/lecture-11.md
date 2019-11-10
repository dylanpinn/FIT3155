# Lecture 11: Network Flow

## Introduction

- `Networks` are `Directed graphs`
- A `flow network` is a connected `directed graph` where
  - there is (often) a single source vertex and a single sink/destination
    vertex;
  - each edge has a stated (non-negative) `capacity`...
  - ...giving the **maximum amount** of `flow` that edge can carry;

## Flow

- Flow is an **assignment** of how much material ('stuff') can flow through each
  edge in the flow network given its stated edge capacity.

**Key property:** `flow conservation`: In a flow network, the amount flowing
`into` and vertex (through all of its incoming edges)... **IS STRICTLY EQUAL
TO** ...the amount flowing `out` of that vertex (through all of its outgoing
edges).

## Basic Notation

- **Flow network**: denoted as $G(V, E, C)$, where
  - $V$ = set of vertices
  - $E$ = set of directed edges
  - $C$ = set of capacities (corresp. to the set of edges, $E$)
- **Source vertex** is denoted as $\textcircled{s}$ (has **no** incoming edges)
- **Sink/Destination vertex** is denoted as $\textcircled{t}$ (has **no**
  outgoing edges)
- **Set of incoming edges** into a vertex $v \in V$ is denoted as $E_{in}(v)$.
- **Set of outgoing edges** from a vertex $v \in V$ is denoted as $E_{out}(v)$.
- **Capacity of any edge** (i.e., the maximum amount of flow an edge can carry)
  $e \in E$ is denoted as $\mathtt{cap}(e)$

## Property 1 of a flow network: Capacity constraint

**Capacity constraint** For each edge $e \in E$, its `flow`, denoted as
`flow(e)`, **is bounded by the capacity** of its edge:
$0 \le \mathtt{flow}(e) \le \mathtt{cap}(e)$.

## Property 2 of a flow network: Flow conservation

**Flow conservation** For any vertex $v$ (that is **not** either `source` or
`sink`), the amount of flow into that vertex from its **in-coming** edges is
same as the amount of flow going out from its **out-going** edges:

$$
\sum_{\forall e_{in} \in e_{in} (v)} \mathtt{flow}(e_{in}) =
\sum_{\forall e_{out} \in e_{out}(v)} \mathtt{flow}(e_{out})
$$

## The value of a flow within the whole network

**Value of a flow** If a flow network satisfies the two properties stated above,
its `value` is the **total flow out of the source vertex**. Equivalently, this
should be the same as the **total flow into sink vertex.**

$$
\text{Flow value } =
\sum_{\forall \langle s,x \rangle \in e_{out}(s)} \mathtt{flow}(\langle s,x \rangle) =
\sum_{\forall \langle y,t \rangle \in e_{in}(t)} \mathtt{flow}(\langle y,t \rangle)
$$

## Maximum-flow problem

**Problem statement:** Given some `flow network`, what is the **maximum**
`value` of the flow that can be sent from source $\textcircled{s}$ to sink
$\textcircled{t}$ **without** violating the `flow conservation` on each vertex
in the network?

## What is the `residual network` for a given flow network?

Given a flow network $G$:

- The **residual** network $G_{residual}$ has the **same number of vertices** as
  the original network $G$.
- However, for every **directed** edge $\langle u,v \rangle$ in the original
  network $G$:
  - there is a directed edge $\langle u,v \rangle$ (in the **same** direction)
    in $G_{residual}$ whose capacity is
    $c( \langle u,v \rangle) - f(\langle u,v \rangle)$, if this quantity is
    greater than 0.
  - there is a directed edge $\langle v,u \rangle$ (in the **reverse**
    direction) in $G_{residual}$ whose capacity is $f(\langle u,v \rangle)$, if
    this quantity is greater than 0.

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8t08nzlx9j30si08h76t.jpg)

### Augmenting path in the residual network

Any `simple path` (i.e., path without repeating vertices) from source $s$ to
sink $t$ in the **residual** network of $G$ is an `augmenting path`.

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8t0jrtafdj30si07zgne.jpg)

**What is an augmenting path useful for?** The flow `value` of $G$ can be
augmented by the **minimum** capacity (or `flow bottleneck`) observed on the
edges along the augmenting path in $G_{residual}$. In the example above, the
`bottleneck` along the augmenting path (shaded edges) is 4. So, the flow in the
original graph can be augmented by 4.

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8t0lsur6tj30si0iswit.jpg)

### Ford-Fulkerson's algorithm - pseudocode

```c
/* Input: (1) flow network G(V,E,C).
          (2) s in V is the source.
          (3) t in V is the sink. */
function Ford_Fulkerson(G, s, t) {
  flow[1..|E|] = 0; // init flow on each edge in G to 0.
  G_residual = G; // init residual network to G. Capacity of edges in
                  // ... G_residual = assigned flow of edges in G.

  while (there exists a path p from s to t in G_residual) {
    // Let path p contain edges {e_1, e_2, ...}
    bottleneck = minimum_i (capacity[e_i]) /* forall e_i in p */

    // augment step
    for (each edge in e_i = <u,v> in p) {
      if (<u,v> in G) {
        flow[<u,v>] = flow[<u,v>] + bottleneck;
      } else {
        flow[<u,v>] = flow[<u,v>] - bottleneck;
      }
    }
    Compute G_residual of G using current flow assignments.
  }

  return flow;
}
```

### Analysis of Ford-Fulkerson's Algorithm

- The running time of Ford-Fulkerson on a network $G(V,E,C)$ depends on how we
  find the augmenting path $p$ and how many times the outer-while loop runs.
- One method for choosing the shortest path is BFS.
  - Number of vertices in $G_{residual} |V|$
  - Number of edges in $G_{residual} \le 2|E|$
  - Therefore, worst-case time to find a path in $G_{residual}$ is
    $O(|V| + 2|E|) = O(|E|)$.
- For a flow network with integer capacities and the `maxium flow value` of
  $\mathtt{Value}_{max}$, the outer while loop executes $\mathtt{Value}_{max}$
  times in the worst-case.
- Therefore, total run-time is $O(|E|\mathtt{Value}_{max})$

### Two strategies to implement of Ford-Fulkerson's general method

Ford-Fulkerson method really does not specify which augmenting path to use if
there is more than one choice to be made.

Two implements that do NOT make arbitrary choices for augmenting paths are:

1. Dinic/Edmonds-Karp augmentation on
   $\textcircled{s} \rightarrow \textcircled{t}$ path with `fewest edges`.
2. Edmonds-Karp augmentation on $\textcircled{s} \rightarrow \textcircled{t}$
   path with `largest bottleneck`.

These two strategies guarantee to run in `polynomial` time.

#### Dinic/Edmonds-Karp augmentation on $\textcircled{s} \rightarrow \textcircled{t}$ path with `fewest edges`

A straightforward approach to find $\textcircled{s} \rightarrow \textcircled{t}$
augmenting path with `fewest edges` is:

- Run BFS from $\textcircled{s}$ to find
  $\textcircled{s} \rightarrow \textcircled{t}$ in $G_{residual}$.

#### Edmonds-Karp augmentation on $\textcircled{s} \rightarrow \textcircled{t}$ path with `largest bottleneck`

A straightforward approach to find $\textcircled{s} \rightarrow \textcircled{t}$
augmenting path with `largest bottleneck` is:

- Grow a spanning tree $M$ starting from $\textcircled{s}$.
- In each iteration, choose the `highest capacity` across the cut defined by the
  vertices in $M$.
- Repeat the above until $M$ grows to contain $\textcircled{t}$.

## Min-cut Max-flow theorem

If $f$ is some flow (assignment) of a network and $(S,T)$ is some cut such that
$$\text{value}(f) = \text{capacity}(S,T)$$ then $(S,T)$ is the
`minimum (capacity) cut`, and, equivalently, $f$ is `maximum flow` in the flow
network.
