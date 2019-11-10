# Lecture 9: Data compression related algorithms

## Content

- Introduction to lossless data compression.
- Fixed and variable length codes.
- Prefix-free code words for encoding/decoding
  - Character streams
  - Integer streams
- A simple dictionary-based compression algorithm on text.

## Lossless compression - encoding and decoding

Lossless data compression algorithms allow encoding the original data into a
compact (encoded) form, and which in turn can be perfectly reconstructed
(decoded) to get back the original data.

### Outcomes and Probability of outcomes

#### Random variables and outcomes

- A `random variable` $x$ is a variable that can take a set of _possible_
  values, $o_1, o_2, \cdots, o_n$.
- Each such possible value is an `outcome` of some (random) event/phenomenon.
  Examples:
  - Throw of dice
  - Coin tosses
  - Occurrence of character in text.
  - etc.
- Associated with each outcome $x=o_i$, there is a `probability` of that
  outcome, denoted by $\Pr(x=o_i)$.

### How do we measure information content of an outcome $x=o_i$?

#### Shannon's `information content` of an outcome

The measure of the information content of an `outcome` $x = o_i$ of a random
variable $x$ is given by: $$I(o_i) = - \log(\Pr(x=o_i))$$

### Shannon's `entropy` over all outcomes

Shannon's `entropy` gives the measure of the `average` information content
across all outcomes of the random variable $x$:
$$ H(x) = \sum_{i=1}^n \Pr(x=o_i)I(o_i)$$

## Huffman coding yields `prefix-free` codes

- Huffman codeine is a method of generating reliable `prefix-free` code words.
- It **requires** as input, the `frequencies` of characters.
- It yields:
  - the shortest code word for the most frequent character.
  - the second shortest code word for the second most frequent character.
  - ...and so on.
- the coding algorithm falls in the class of `greedy algorithms`.

### Huffman coding algorithm summary

1. Compute frequencies of each unique character in the given text/data.
2. Imagine each character as a leaf node in a binary tree you are constructing.
3. Repeatedly join two characters/nodes with the smallest frequencies to form a
   new node.
   - This new node represents the sum of frequencies of nodes that were joined.
   - Assign a bit symbol `0` to the left branch.
   - Assign a bit symbol `1` to the right branch.
4. Stop repeating step 3 when all nodes are joined into a rooted binary tree.
5. Each character's code-word is then the sequence of `0`s and `1`s generated
   from `root-to-leaf` traversal on that binary tree.

## Elias (Omega) code for universal integers

By universal integers, we are considering positive integers from
$1, 2, \ldots, \infty$.

### Overarching strategy

The strategy to design a code work for an integer $N$ is:

- Encode $N$
- Encode $L_1$ = length($N$) - 1
- Encode $L_2$ = length($L_1$) - 1
- Encode $L_3$ = length($L_2$) - 1
- $\cdots$
- $\ldots$ and so on until the final encoded length is 1.

We will call the encodings of $L_1, L_2, \cdots$ as the `length component`, and
the encoding of $N$ as the `code component`.

### Decoding can be problematic

Encoding $N, L_1, L_2, \ldots$ integers using directly their **minimal binary
codes** poses a problem.

- During decoding, we cannot differentiate between the `length components` and
  the actual `code component` of $N$.

Elias (omega) encoding of integers addresses this problem by changing the
most-significant `1` in the **minimal binary code** of each `length component`
to `0`.

### Decoding

1. Input: `codeword[1...]`
2. Initialise: `readlen` $= (1)_{dec}$, `component = <EMPTY>, pos = 1`
3. `component = codeword[pos...post + readlen - 1]`.
4. If the **most-significant** bit of a `component` is `1`, then
   `N = (component)`. **STOP**.
5. Else, if the **most-significant** bit of a `component` is `0`, then flip
   $0 \rightarrow 1$ and reset `pos = pos + readlen, readlen = (component) + 1`.
6. Repeat from step 2. until $N$ is decoded (when step 3 is true).

## Lempel Ziv algorithms

### Lempel-Ziv (LZ77) algorithm

- LZ77 is a **sliding window** based algorithm.
- Since original publication, it inspired many variants (e.g. LZSS).
- Used in many applications: `gzip`, `PKZIP`, etc.

#### Basic strategy

- The LZ77 encoding involves examining the input text through a sliding window.
- The window consists of 2 consecutive parts:
  1. search window (also called the '`dictionary`')
  2. lookahead buffer (sometimes called the '`buffer`')
- To encode any char/substring in the lookahead buffer:
  - Find the `largest` matched substring in the `dictionary` (i.e., search
    window).
  - This yields three pieces of information:
    1. The `offset` (i.e., distance of the match from the current char/substring
       being encoded).
    2. The `length` of the match.
    3. The next character `char` in the lookahead buffer, after that matched
       char/substring.
- Using this search, the char/substring at the current position is encoded as a
  **triple** `<offset, length, char>`.

#### Decoding

- Decoding is straightforward using the triple encoding we just saw.
- Using the same sliding window size (=dictionary size + lookahead buffer size),
  decode the text left to right, using one triple at a time.

### LZSS (Lempel-Ziv-Storer-Szymanski) variation of LZ77 algorithm

LZSS variant of LZ77, improves the original LZ77 by reducing the amount of space
required to encode short substrings as triples. This is achieved by using two
formats for encoding character/substrings during encoding.

1. `Format 0:` When the `length` of the matched substring in the `dictionary`
   $\ge 3$, use: `<0-bit, offset, length>`
2. `Format 1:` When the `length` of the matched substring in the `dictionary`
   $< 3$, use: `<1-bit, char>`.
