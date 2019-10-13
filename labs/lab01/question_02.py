"""
FIT3155 - Lab 2

Question 2

Implement a naive exact pattern matching algorithm.

Dylan Pinn - 24160547
"""


def naive(pat, txt):
    n = len(txt)
    m = len(pat)
    if m > n:
        return False
    for i in range(0, n - m + 1):
        j = 0

        while j < m:
            if txt[i + j] != pat[j]:
                break  # mismatch
            j += 1

        if j == m:
            return True

    return False
