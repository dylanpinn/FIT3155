# Lecture 8: (Semi-)numerical algorithms

## Content

- Algorithms involving (large) numbers
  - Integer multiplication
  - Modular exponentiation
  - Miller-Rabin Primality Testing

## Introduction

- Number-theoretic algorithms are used widely today.
- Most prominent use is cryptographic schemes.
- These schemes rely on **large prime numbers.**
- The **feasibility** of cryptographic schemes rely on the ability to generate
  large prime numbers.
- The **security** of cryptographic schemes rely on the **in**ability to
  efficiently **factorise** large numbers into their prime factors.

## Computational complexity as a function of a size of input

- For the algorithms here, we need to change the way we think about the size of
  input.
- For instance, in sorting algorithms, we thought of the size of input in terms
  of the number of elements being sorted.
- Here, we will measure the input in terms of **number of bits** required to
  represent the input.
- For an integer $n$, the **number of bit** it takes to represent is
  $d = \lfloor \log n \rfloor + 1$ bits.
- So, a number-theoretic algorithm runs...:
  - ...in `linear` time, if it involves $O(d)$ computations.
  - ...in `quadratic` time, if it involves $O(d^2)$ computations.
  - etc.
  - ...in `logarithmic` time, if it involves $O(\log d)$ computations.

## Fast multiplication algorithm on (large) integer

### $O(d^{\log_2 3})$-time integer multiplication

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8qk1r5l3dj30vo0gejv6.jpg)

$$
uv = (2^{2d} + 2^d)U_1 V_1 - 2^d(U_1 - U_0)(V_1 - V_0) + (2^d + 1)U_0 V_0
$$

The form above decomposes the multiplication $uv$ (problem of multiplying two
$2d$-bit numbers) into:

- Three $d$-bit multiplications:
  1. $U_1 V_1$
  2. $(U_1 - U_0)(V_1 - V_0)$
  3. $U_0 V_0$
- plus some simple left shifting
  - multiplication by and $2^k$ requires shifting the bits leftwards by $k$
    positions.
- and some additions/subtractions.

#### Time Complexity

The time complexity of this divide-and-conquer approach can be expressed using
the recurrence relationship: $T(2d) = 3T(d) + cd$, where $c$ is some constant.
Solving this recurrence yields the $O(d^{\log_2(3)})$-time algorithm.

### Divisibility and Divisors

The notion of one integer being `divisible` by another is key to theory of
numbers.

#### Division theorem

For any integer $a$ and any positive integer $n$, there exists unique integers
$q$ (quotient) and $r$ (remainder) such that $a = qn + r$, were $0 \le r < n$.

#### Quotient

The value $q = \lfloor \frac{a}{n} \rfloor$ is the `quotient` of the division.

#### Remainder

The value $a \mod n = r$ is the `remainder` (sometimes called residue) of
division.

### Congruence class modulo $n$

When dividing integers by $n$, we can divide them into $n$ `congruence classes`,
based on the remainder $r (0 \le r < n)$ that each integer leaves.

#### Congruence class definition

Two integers $a$ and $b$ are in the same congruence class modulo $n$,
`if and only if` $(a-b)$ is an `integer multiple` of $n$. This relationship is
denoted as:

$$a \equiv b \mod n$$

Another way to look at this: Two integers $a$ and $b$ are in the same congruence
class modulo $n$, `if and only if` the remainder when $a$ is divided by $n$ is
same as the remainder when $b$ is divided by $n$.

## Modular exponentiation ($a^b \mod n$) on large integers

### Modular Exponentiation

- A frequently occurring operation in number-theoretic computations is raising
  one number to a power, and then modulo dividing with another number.
  $$a ^b \mod n$$

- This is known as `modular exponentiation`.
- For small integers, we can first compute $a^b$ and then modulo divide the
  result with $n$ to get a final answer.
- However, this method is infeasible when dealing with large numbers. Example:
  $$1729^{1023} \mod 75$$
- A popular algorithm for modular exponentiation is the method of
  `repeated-squaring`.

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8ql27cujtj30vo0jw41g.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8ql7ji6zrj30vo0mytcx.jpg)

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g8ql7ujkvmj30vo0myjwy.jpg)

## Prime

### Naive Algorithm for Primality testing - trail division

```c
function naive_test1(n) {
  for (k in the range 2 and n-1) {
    if (n mod k == 0) return "Composite";
  }
  return "Prime";
}
```

#### Complexity

- $O(n)$ number of divisions
- Basic division algorithms between two $d$-bit integers is $O(d^2)$.
  - A (decimal) number $n$ requires $d = \lfloor \log (n) \rfloor + 1$ bits to
    represent. Therefore each division is $O(d^2)$
- Therefore, total complexity is $O(nd^2)$-time using the naive algorithm above.
- However, this can be reduced to $(\sqrt{nd^2})$-time.

## Fermat's little theorem

If $p$ is a **prime number**, then for any integer $a$, the number $a^p - a$ is
an **integer multiple** of $p$. In the language/notation of **modular
arithmetic**, this is expressed as $$a^p \equiv a \mod p$$

If $a$ is **not divisible by** $p$, Fermat's little theorem stated above is
`equivalent` to the statement that $a^{p-1} -1$ is an integer multiple of $p$:
$$a^{p-1} \equiv \mod p$$

### Randomized Fermat Test

Before anything, we only care about primality testing when $n$ is `odd`. For
even $n$, one can return 'Composite' without the test below.

```c
function FermatRandomisedTest(n) {
  a = choose random number in the range 1 < a < n
  if (a^{n-1} modulo n  != 1)
    return "Composite"
  return "PROBABLY Prime"
}
```

- Unfortunately, this test is necessary but not sufficient.
- It tests for primality only probabilistically.
- That is, on rare occasions there are composite numbers (Carmicheal numbers)
  which this test returns a 'Probably Prime' answer.
- How rarely does this fail?
  - There are only 22 values of $n < 100,000$ for which this test fails.

## Miller-Rabin Test

Miller-Rabin primality testing tries to overcome this problem with two
modifications.

1. The algorithm test several `randomly` chosen base values of $a$ instead of
   just one used previously.
2. In each test, when computing the modular exponentiation $a^{p-1}$, it makes
   use of some key observations, that reduces the chance of falsely calling a
   'composite' number 'probably prime'.

Note, testing primality of $n$ involves testing only when $n$ is `odd`. Even
numbers, on the otherhand, can be trivially returned as 'composite'.

### Observation 1

If $n$ is an `odd` number, then $n - 1$ can be represented as $$n - 1 = 2^s.t$$
where $t$ is some odd number.

### Observation 2

Given $n$ is odd, and $n-1 = 2^s.t$, where $t$ is odd, if

$$
a^{2^i .t} \mod n \text{ and } a^{2^{i-1}} \not\equiv \pm 1 \mod n,
0 < i \le s, 1 < a < n-1
$$

Then, $n$ **has to be composite.**

#### Intuition for Observation 2

- $n - 1 = 2^s . t$
- $\Rightarrow a^{n-1} \mod n = a^{2^s .t} \mod n$.
- We will compute $a^{2^s .t} \mod n$ iteratively starting with...
- ...$a^{2^0 .t} \mod n$ (denoted as $x_0$).
- This result is progressively squared (modulo $n$) yielding:
  - $\ldots a^{2^1 .t} \mod n$ (denoted as $x_1$), which in turn yields
  - $\ldots a^{2^2 .t} \mod n$ (denoted as $x_2$), which in turn yields
  - $\ldots a^{2^3 .t} \mod n$ (denoted as $x_3$), which in turn yields
  - ...and so on until
- This successive squaring method yields a sequence of numbers:
  $$\langle x_0, x_1, x_2, \cdots, x_s \rangle$$
- The following `cases` apply to this sequence:
  $\langle x_0, x_1, x_2, \cdots, x_s \rangle$
  1. $x_s = r \ne 1$. That is, the sequence does **not** end with $x_s = 1$
     result.
     - Return 'Composite'
  2. Some $x_{i-1} = r \ne \pm 1$, and $x_i = 1$. That is, the sequence is
     $\langle \cdots, r,1,1,1,\cdots,1\rangle$.
     - Return 'Composite'
  3. Some $x_{i-1} = -1$, and $x_i = 1$. That is, the sequence is of the form:
     $\langle \cdots, -1,-1,1,1,\cdots,1\rangle$.
     - Return 'Probably Prime'
  4. $x_0=x_1=x_2=\cdots=x_s=1$. That is, the sequence is `all` **ones**.
     - Return 'Probably Prime'

### Miller-Rabin's Randomized Primality testing algorithm

```c
/*  Input: n > 2, is the number being tested for primality
    Input: k, a parameter that determines accuracy of the test */
function MillerRabinRandomizedPrimality(n,k) {
  if (n is even) return "Composite";
  /* Factor n-1 as 2^s.t, where t is odd */
  s = 0, t = n-1;
  while (t is even) {
    s = s + 1;
    t = t / 2;
  } // at this stage, n-1 will be 2^s.t, where t is odd.
  /* k random tests */
  loop (k times) {
    a = choose random number in [2..n-1);
    if (a^{n-1} modulo n != 1) return "Composite";
    for (i in [1...s]) {
      if (a^{2^i.t} modulo n == 1 &&
          a^{2^{i-1}.t} modulo n != (+1 or -1))
          return "Composite";
    }
  }
  return "Probably Prime"; // accuracy depends on k.
}
```

### Accuracy of Miller-Rabin's Algorithm

- The more the number of $a$'s that are tested, the greater the accuracy of this
  test.
- There is a proof that show that this algorithm declares a composite number
  incorrectly prime with a probability of at most $\frac{1}{4^k}$, over $k$
  tests.
- That is, if $k=64$, then the probability of a given odd composite number $n$
  to be incorrectly called prime is $\frac{1}{2^{128}}$.
