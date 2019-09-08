"""Modified KMP Algorithm.

"""


def match(pat, txt):
    """Does pattern exist in text."""
    n = len(txt) - 1
    m = len(pat) - 1

    for i in range(0, n - m + 1):
        for j in range(0, m + 1):
            if txt[i + j] != pat[j]:
                break
            if j == m:
                return True
    return False
