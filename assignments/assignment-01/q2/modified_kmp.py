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
    """
    # Preprocess pattern
    suffix_prefix = compute_suffix_prefix(pat)
    n = len(txt) - 1
    m = len(pat) - 1
    matches = []

    for i in range(0, n - m + 1):
        for j in range(0, m + 1):
            if txt[i + j] != pat[j]:
                break
            if j == m:
                matches.append(i + index)
                break
    return matches


def match(pat, txt):
    """Does pattern exist in text.
    :param pat: str
    :param txt: str
    """
    result = kmp(pat, txt)
    return len(result) > 0
