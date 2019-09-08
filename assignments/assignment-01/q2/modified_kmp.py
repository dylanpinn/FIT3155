"""Modified KMP Algorithm.

"""

from q2.z_algorithm import find_z_array


def compute_suffix_prefix(pat):
    """Preprocess Suffix prefix length of pattern.
    :param pat: str
    """
    m = len(pat) - 1
    suffix_prefix = [0] * (m + 1)
    z_suffix = find_z_array(pat)

    for j in range(m, 0, -1):
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
            shift = i - suffix_prefix[i - 1]

        j += max(shift, 1)

    return matches


def match(pat, txt):
    """Does pattern exist in text.
    :param pat: str
    :param txt: str
    """
    result = kmp(pat, txt)
    return len(result) > 0
