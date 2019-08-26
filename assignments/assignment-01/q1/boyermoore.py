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

# Boyer-Moore Algorithm

# Preprocess step
#   bad-chacater shift jump tables
#   goodsuffix & matchedprefix values for good suffix shifts


# Bad characater shift rule

# Good suffix
def calculate_goodsuffix(pattern):
    """Calculate good suffix values of pattern."""
    m = len(pattern)
    goodsuffix = []
    for j in range(m + 1):
        goodsuffix[j] = 0
        print(j)


def matches(pat, txt):
    """Simple check if the pat matches against txt."""
    calculate_goodsuffix(pat)
    return True


if __name__ == '__main__':
    # executed directly
    print(matches('abc', 'abcd'))
