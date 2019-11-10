# Lecture 10: Linear Programming

## Linear Programming problem in its standard form

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8sw11a6byj30s50fcabf.jpg)

## Graphical Solution

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8sw2a5ifwj30r90ibmyr.jpg)

**Feasible region** is the region where the given linear program has
`feasible solutions` **satisfying** all its constraints.

**Insight 1** Feasible region is a **convex polyhedron**.

**Insight 2** For **any point** in the `feasible region`, **there is always a
point** `on the boundary` of the feasible region that will `dominate` it (i.e.,
will give a better evaluation of the `objective function`).

**Insight 3** Further, **among all points of the boundary** of the feasible
regions, there is **at least** `one corner point` of the feasible region that
will always `dominate`, given the objective function.

## Algebraic Solution

- An important step here it to convert the `inequality` constraints into
  `equality` constraints.
- This is achieved by adding `slack variables` to convert an inequality to an
  equality.

### Changing inequality constraints into equality constraints

First constraint: $x + y \le 5$ becomes $$x + y + x = 5$$ where $s \ge 0$.

Similarly the second constraint $3x + 2y \le 12$ becomes $$3x + 2y + t = 12$$
where $t \ge 0$.

Objective function can be written as: $$\text{Maximise } z = 6x + 5y$$

### Formulation of the problem

Therefore, solving this problem:

Maximise $$z = 6x + 5y$$ Subject to the constraints $$x + y \le 5$$
$$3x + 2y \le 12$$ and $x, y \ge 0$

is the same as solving this problem:

Maximise $$z = 6x + 5y$$ Subject to the constraints $$x + y + s = 5$$
$$3x + 2y + t = 12$$ and $x, y, s, t \ge 0$

There are 4 variables and 2 equations. Solutions can only be found for any 2
variables, if the remaining 2 variables are 'fixed'.

### Possible ways of fixing variables

|            |                      |
| ---------- | -------------------- |
| Fix $x, y$ | and solve for $s, t$ |
| Fix $x, s$ | and solve for $y, t$ |
| Fix $x, t$ | and solve for $y, s$ |
| Fix $y, s$ | and solve for $x, t$ |
| Fix $y, t$ | and solve for $x, s$ |
| Fix $s, t$ | and solve for $x, y$ |

By fixing the variables in the left column to zeros, we get:

| `Non-Basic Variables` | `Basic Variables`      |
| --------------------- | ---------------------- |
| Fixing $x = 0, y = 0$ | We get $s = 5, t = 12$ |
| Fixing $x = 0, s = 0$ | We get $y = 5, t = 2$  |
| Fixing $x = 0, t = 0$ | We get $y = 6, s = -1$ |
| Fixing $y = 0, s = 0$ | We get $x = 5, t = -3$ |
| Fixing $y = 0, t = 0$ | We get $x = 4, s = 1$  |
| Fixing $s = 0, t = 0$ | We get $x = 2, y = 3$  |

#### Non-basic variables

- `Non-basic` variables are the variables that are `fixed` to **zero**.
- The are so called, because they are **OUTSIDE** the **basis** of the linear
  programming problem.

#### Basic variables

- The remaining `free` variables are called `basic variables`.
- Basic variables are those that are **WITHIN** the **basis** of the linear
  programming problem.

### Exhaustive search

Objective $$z = 6x + 5y$$

| `Non-Basic Variables` | `Basic Variables`      | value of objective |
| --------------------- | ---------------------- | ------------------ |
| Fixing $x = 0, y = 0$ | We get $s = 5, t = 12$ | $z = 0$            |
| Fixing $x = 0, s = 0$ | We get $y = 5, t = 2$  | $z = 25$           |
| Fixing $x = 0, t = 0$ | We get $y = 6, s = -1$ | **Infeasible**     |
| Fixing $y = 0, s = 0$ | We get $x = 5, t = -3$ | **Infeasible**     |
| Fixing $y = 0, t = 0$ | We get $x = 4, s = 1$  | $z = 24$           |
| Fixing $s = 0, t = 0$ | We get $x = 2, y = 3$  | $z = 27$           |

### Generalising this Algebraic (graphical) method

- Let some general linear programming formulation contain:
  - $N$ `decision variables`
  - $m$ `linear constraints`
- For $m$ linear constraints, there will be $m$ **slack variables**.
- There are $N$ `decision variables` and $m$ `linear equations` in this system.
- Assign $N$ out of $N + m$ (`decision + slack`) variables to 0, and solve for
  the remaining $m$ variables.
- There are ${N+m}\choose{n}$ possibilities.
- Substitute the values of that $N$ `decision variables` take into the objective
  function.
- Once all possibilities are explored, choose the **optimum** over all the
  solutions.

#### Disadvantages of Algebraic (graphical) method

- Grows combinatorially large for $N$
- Evaluates **infeasible solutions.**
- Does not tell you if the optima has been reached. The search is exhaustive
  (brute-force).
- Does not give progressively better solutions - the search is fairly random.

## Simplex Method to solving linear programming problems

Simplex Method is a way to solve this problem. Advantages of simplex are:

- Polynomial time (**in practice**, but not in **worst case**)
- Does **NOT** evaluate **infeasible solutions.**
- Explorers `progressively better solutions`.
- Tells you when the optima has been reached and stops.

### Explored in two forms

Two forms on the simplex methods using the same example as earlier:

- Algebraic form of simplex: **this will provide insights for what it is
  doing**.
- Tabular (or tableau) form of a simplex: **this will all us to crank-turn
  easily**.

### Algebraic Form

Maximise $$z =6x + 5y$$ Subject to the constraints: $$x + y + s = 5$$
$$ 3x + 2y + t = 12$$ and $x, y, s, t \ge 0$.

#### Start

Start by choosing $x$ and $y$ as `non-basic variables` (i.e., variables that are
set to 0.)

This gives the solutions to $s$ and $t$ as $s = 5$ and $t = 12$ respectively.

#### First Iteration

Rewrite the constraints in terms of $s$ and $t$ (now basic variables)
$$s = 5 - x - y$$ $$t = 12 - 3x - 2y$$ Objective is simply: $z = 6x + 5y$.

- Recall, currently, $x = 0$ and $y = 0$. Therefore the objective function,
  substituting these values is, $z = 0$. Can we improve $z$?
- Yes. We can either `increase` the value of $x$ or `increase` the value of $y$.
- In simplex, you can only improve `one variable` at a time.
- Choose to increase $x$ **(since it has a larger coefficient of the two
  choices, hence gives higher increase of the objective**).
- However, having chosen to increase $x$, we can either increase it:
  - from $x = 0$ to $x = 5$ according to the `first` constraint. **Anything more
    will violate the `non-negativity constraint` for the slack variable $s$.**
    Or
  - from $x = 0$ to $x = 4$ according to the `second` constraint. **Anything
    more will violate the `non-negativity constraint` for $t$.**
- Choosing the `minimum` of $x = 5$ and $x = 4$ will ensure that both
  $s, t \ge 0$.
- Since we have chosen the `minimum increase` of $x$ from $x = 0$ to $x = 4$,
  **$x$ enters the basis**, while **$t$ exists the basis**
  $(x = 4, \Rightarrow t = 0)$.
- The new set of `non-basic variables` are therefore $y$ **and** $t$, and
  `basic variables` are $x$ **and** $s$. That is $x = 4, s = 1, y = 0, t = 0$.

##### Rewrite the constraints in terms of the new basic variables

Rewrite the second constraint $(t = 12 - 3x - 2y)$, now with $x$ as the
`basic variable`: $$x = 4 - \frac{2}{3}y - \frac{1}{3}t$$ The first constraint
in the previous iteration was $s = 5 - x - y$. Rewriting this by substituting
$x$ from above, becomes: $$s = 1 - \frac{1}{3}y + \frac{1}{3} t$$

#### Second Iteration

Problem as it is now transformed $$x = 4 - \frac{2}{3} y - \frac{1}{3} t$$
$$s = 1 - \frac{1}{3} y + \frac{1}{3} t$$ Objective was previously to maximise:
$$z = 6x + 5y$$ now becomes (in terms of the new `non-basic` variables $y$ and
$t$) $$z = 24 + y - 2t$$

**Notice how the objective function is growing** Previously, $z = 0$ (with $x$
and $y$ as the non-basic variables). Now, $z = 24$ when $y = 0$ and $t = 0$ are
the non-basic variables.

#### Third Iteration

(Note: What we are doing here is a **repetition** of the steps/logic undertaken
in the previous iteration)

- To increase $z$ further, we can either `increase` $y$ (since coefficient in
  the objective is `positive`) or `decrease` $t$ (since the coefficient in the
  objective is `negative`.
- Decreasing $t$ is **infeasible** because $t$ is already zero and any further
  will **violate** non-negativity constraint. Therefore, our only choice here is
  to `increase` $y$.
- However, $y$ can only be increased from $y = 0$ to $y = 3$ (based on the
  second equation) for the solution to be feasible.

Since we have chosen to **increase `y` from 0 to 3**, the new `basic variables`
are $x, y$ whose current values are $x = 2$ and $y = 3$ and the
`non-basic variables` are $s = 0, t = 0$.

##### Rewrite the constraints in terms of the new basic variables

We write the second equation $(s = 1 - \frac{1}{3} y + \frac{1}{3} t)$ with $y$
as the `basic variable`: $$y = 3 - 3s + t$$ But, the first equation in the
iteration is $x = 4 - \frac{2}{3} y - \frac{1}{3} t$. Rewriting this by
substituting $y$ from above, we get: $$x = 2 + 2s -t$$

##### Problem as it is now transformed

$$x = 2 + 2s - t$$ $$y = 3 - 3s + t$$ Objective was to maximise:
$$z = 24 + y - 2t$$ now becomes (in terms of new `non-basic variables`)
$$z = 27 - 3s - t$$

Observe that $z = 27$ when $s = 0$ and $t = 0$ as the new `non-basic variables`.
Can $z$ be increased further?

The only way to increase $z$ further is to either `decrease` $s$ and/or
`decrease` $t$. Both of these choices are **infeasible therefore STOP.**

### Tableau form of Simplex does `exactly` the same thing but in a convenient tabular way

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8synxw01ij30id0df3zj.jpg)
