#!/usr/bin/env python3

"""Modified KMP Algorithm."""

import sys

from z_algorithm import find_z_array

ALPHABET_SIZE = 256


def modified_suffix_prefix(pat):
    """Calculate modified suffix prefix.
    :param pat: str
    """
    m = len(pat)
    suffix_prefix = [[0] * ALPHABET_SIZE] * m
    z_suffix = find_z_array(pat)

    for j in range(m - 1, 0, -1):
        i = j + z_suffix[j] - 1
        x = pat[z_suffix[j] + 1]
        suffix_prefix[i][ord(x)] = z_suffix[i] if z_suffix[i] is not None else 0

    return suffix_prefix


def compute_suffix_prefix(pat):
    """Preprocess Suffix prefix length of pattern.
    :param pat: str
    """
    m = len(pat)
    suffix_prefix = [0] * m
    z_suffix = find_z_array(pat)

    for j in range(m - 1, 0, -1):
        i = j + z_suffix[j] - 1
        suffix_prefix[i] = z_suffix[j]
    return suffix_prefix


def kmp(pat, txt, index=1):
    """Knuth-Morris-Pratt (KMP) Algorithm.
    :param pat: str
    :param txt: str
    :param index: int Offset results index
    """
    n = len(txt)
    m = len(pat)
    matches = []

    if m > n:
        return matches
    # Preprocess pattern
    mod_suffix_prefix = modified_suffix_prefix(pat)
    suffix_prefix = compute_suffix_prefix(pat)

    j = 0
    while j <= n - m:
        i = 0

        while i < m and pat[i] == txt[i + j]:
            i += 1

        if i == m:
            # Full match
            matches.append(j + index)
            shift = m - suffix_prefix[m - 1]
        else:
            # Mismatch
            x = txt[i + j]
            if i > 0:
                shift = i - mod_suffix_prefix[i][ord(x)]
            else:
                shift = 1
        j += max(shift, 1)

    return matches


def match(pat, txt):
    """Does pattern exist in text.
    :param pat: str
    :param txt: str
    """
    result = kmp(pat, txt)
    return len(result) > 0


def output_result(results):
    output_name = 'output_kmp.txt'
    with open(output_name, 'a') as file:
        for line in results:
            file.write("%s\n" % line)


if __name__ == "__main__":
    # executed directly
    input_text = open(sys.argv[1], 'r')
    pattern_text = open(sys.argv[2], 'r')
    text = input_text.read()
    pattern = pattern_text.read()
    text, pattern = text.rstrip(), pattern.rstrip()
    output = kmp(pattern, text)
    output_result(output)
