"""Boyer-Moore's Algorithm

Given some text txt[1...n] and a pattern pat[1...m], implement Boyer-Moore's
algorithm to find all occurrences of pat in txt.
Implementation should use the following:

 - extended bad-character rule
 - the good-suffix rule (using good_suffix and matched_prefix data structures),
 - the Galil's optimisation to avoid any unnecessary character comparision.

arguments: two plain text files:
 - an input file containing txt[1...n] (without any line breaks)
 - an input file containing pat[1...m] (without any line breaks).

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
    bad_character_shift = [-1 for a in range(ALPHABET_SIZE)]

    for i, _ in enumerate(pattern):
        bad_character_shift[ord(pattern[i])] = i

    return bad_character_shift


def calculate_good_suffix(pattern):
    """Calculate good suffix values of pattern."""
    # Instantiate good suffix array with 0 values.
    m = len(pattern)
    good_suffix = [-1] * (m + 1)

    z_suffix = find_z_array(reverse_string(pattern))
    z_suffix.reverse()

    for p in range(0, m - 1):
        j = m - z_suffix[p]
        good_suffix[j] = p
    return good_suffix


def calculate_matched_prefix(pattern):
    """Calculate matched prefix values of pattern."""
    matched_prefix = find_z_array(pattern)

    j = 0
    for i in range(len(matched_prefix) - 1, -1, -1):
        if matched_prefix[i] == len(pattern) - 1:
            j = max(j, matched_prefix[i])
        matched_prefix[i] = j

    return matched_prefix


def boyer_moore(pat, txt, index=1):
    """Check for pattern matches using Boyer-Moore's algorithm."""
    # No match if pat is longer than txt.
    if len(pat) > len(txt):
        return []

    # TODO: Add Galil's improvements.

    # Pre-process
    bad_char_shift = calculate_bad_char_shift(pat)
    good_suffix_table = calculate_good_suffix(pat)
    matched_prefix = calculate_matched_prefix(pat)

    j = 0
    m = len(pat) - 1
    n = len(txt) - 1
    matches = []

    while j + m <= len(txt):
        k = m  # where we are matching in pat

        while pat[k] == txt[j + k - 1] and k >= 0:
            k -= 1

        # Match is found
        if k == -1:
            matches.append(j + k + index)  # adjust index by 1 for result.
            # case 2: when match is found shift pat by m - matched_prefix[2]
            j += max(1, m - matched_prefix[2] if m > 1 else 1)
        else:
            x = txt[j + k - 1]
            y = pat[k]
            # Calculate bad_character shift jump
            bad_char_shift_jump = max(1, k - bad_char_shift[ord(x)])

            # Calculate good suffix jump
            good_suffix = good_suffix_table[k]
            good_suffix_shift = 0
            # case 1a good_suffix > 0
            if good_suffix > 0:
                good_suffix_shift = m - good_suffix
            # case 1b: good_suffix = 0
            elif good_suffix == 0:
                good_suffix_shift = m - matched_prefix[k]

            j += max(bad_char_shift_jump, good_suffix_shift)
    return matches


def match(pat, txt):
    """Check if the pat matches against txt using Boyer-Moore's algorithm."""
    result = boyer_moore(pat, txt)
    return len(result) > 0


if __name__ == "__main__":
    # executed directly
    # TODO: Read filenames from arguments.
    print(match("abc", "abcd"))
