"""Boyer-Moore's Algorithm

Given some text txt[1...n] and a pattern pat[1...m], implement Boyer-Moore's
algorithm to find all occurences of pat in txt.
Implementation should use the following:

 - extended bad-character rule
 - the good-suffix rule (using goodsuffix and matchedprefix data structures),
 - the Galil's optimisation to avoid any unnecessary chracter comparisions.

arguments: two plain text files:
 - an input file containing txt[1...n] (without any line breaks)
 - an input file containing pat[1...m] (winthout any line breaks).

CLI usage of script:
boyermoore.py <txt file> <pat file>
Output file name: output_boyermoore.txt
  each position where pat matches txt should appear in a separate line.
"""

from z_algorithm import find_z_array

ALPHABET_SIZE = 256

def reverse_string(string):
    """Reverse string using a slice."""
    return string[::-1]


def calculate_bad_char_shift(pattern):
    """Calculate bad character shift rule."""

    # Characters can be {|A-Z|,|a-z|,|0-9|}
    bad_chararacter_shift = [-1 for a in range(ALPHABET_SIZE)]

    for i, _ in enumerate(pattern):
        bad_chararacter_shift[ord(pattern[i])] = i

    return bad_chararacter_shift


def calculate_goodsuffix(pattern):
    """Calculate good suffix values of pattern."""
    # Instantiate goodsuffix array with 0 values.
    m = len(pattern)
    goodsuffix = [-1] * (m + 1)

    z_suffix = find_z_array(reverse_string(pattern))
    z_suffix.reverse()

    for p in range(0, m - 1):
        j = m - z_suffix[p]
        goodsuffix[j] = p
    return goodsuffix


def calculate_matchedprefix(pattern):
    """Calculate matched prefix values of pattern."""
    matched_prefix = find_z_array(pattern)

    j = 0
    for i in range(len(matched_prefix) - 1, -1, -1):
        if matched_prefix[i] == len(pattern) - 1:
            j = max(j, matched_prefix[i])
        matched_prefix[i] = j

    return matched_prefix


def naive_algorithm(pat, txt):
    """Naive implementation of algorithm."""
    if len(pat) > len(txt):
        return False
    for iter in range(0, len(txt)):
        m = len(pat) - 1
        n = len(txt) - 1 - iter
        match = True
        while match is True and m >= 0:
            if pat[m] == txt[n]:
                m -= 1
                n -= 1
            else:
                match = False
        if match:
            return match
    return False


def boyer_moore(pat, txt):
    """Check for pattern matches using Boyer-Moore's algorithm."""
     # No match if pat is longer than txt.
    if len(pat) > len(txt):
        return []

    # TODO: Add Galil's improvements.

    # Pre-process
    badcharshift = calculate_bad_char_shift(pat)
    goodsuffix_table = calculate_goodsuffix(pat)
    matchedprefix = calculate_matchedprefix(pat)

    j = 0
    m = len(pat) - 1
    n = len(txt) - 1
    matches = []

    while j + len(pat) <= len(txt):
        k = m  # where we are matching in pat

        while pat[k] == txt[j + k - 1] and k >= 0:
            k -= 1

        # Match is found
        if k == -1:
            matches.append(j + k + 1)  # adjust index by 1 for result.
            # case 2: when match is found shift pat by m - matchedprefix[2]
            j += max(1, m - matchedprefix[2] if m > 1 else 1)
        else:
            x = txt[j + k - 1]
            y = pat[k]
            # Calculate badcharacter shift jump
            badcharshift_jump = max(1, k - badcharshift[ord(x)])

            # Calculate good suffix jump
            goodsuffix = goodsuffix_table[k]
            goodsuffix_shift = 0
            # case 1a goodsuffix > 0
            if goodsuffix > 0:
                goodsuffix_shift = m - goodsuffix
            # case 1b: goodsuffix = 0
            elif goodsuffix == 0:
                goodsuffix_shift = m - matchedprefix[k]

            j += max(badcharshift_jump, goodsuffix_shift)
    return matches


def matches(pat, txt):
    """Check if the pat matches against txt using Boyer-Moore's algorithm."""
    result = boyer_moore(pat, txt)
    return len(result) > 0


if __name__ == "__main__":
    # executed directly
    # TODO: Read filenames from arguments.
    print(matches("abc", "abcd"))
