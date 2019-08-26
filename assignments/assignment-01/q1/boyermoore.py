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


def find_z_array(string):
    """Calcualte Z-Array using Gusfields Algorithm."""
    z_array = [None] * len(string)
    r_array = [None] * len(string)
    l_array = [None] * len(string)

    match = False
    i = 1
    z_array[1] = 0
    z_index = 1
    if string[i] == string[i-z_index]:
        match = True
        z_array[z_index] += 1
    else:
        match = False
        z_array[z_index] = -1
    while match:
        i += 1
        if string[i] == string[i-z_index]:
            z_array[z_index] += 1
        else:
            match = False

        if z_array[z_index] > 0:
            r_array[z_index] = z_array[1]
            l_array[z_index] = 1
        elif z_array[z_index] == 0:
            r_array[z_index] = 0
            l_array[z_index] = 0

    for k in range(len(string)):
        if k < 2:
            continue

        # Case 1, if k > r:
        # Compute Zk by comparing str[k...q-1] with str[1...q-k] until
        # mismatch is found
        # at some q >= k.
        # if Zk > 0
        #   set rk to q-1
        #   set lk to k
        # else l,r to previous values
        if k > r_array[k-1]:
            match = False
            z_array[k] = 0
            i = 0
            if string[k] == string[1]:
                match = True
                z_array[k] += 1
            else:
                match = False
            while match:
                i += 1
                if string[k + i] == string[i]:
                    z_array[k] += 1
                else:
                    match = False
            if z_array[k] > 0:
                l_array[k] = k
                r_array[k] = k + i - 1
            else:
                l_array[k] = l_array[k-1]
                r_array[k] = r_array[k-1]

        else:
            # Case 2a, if Z_{k-l+1} < r-k+1:
            # set Z_k = Z_{k-l+1}
            # l, r remain unchanged
            l = l_array[k-1]
            r = r_array[k-1]
            if z_array[k - l] < r - k + 1:
                z_array[k] = z_array[k - l]
                l_array[k] = l_array[k-1]
                r_array[k] = r_array[k-1]
            else:
                # Case 2b
                match = False
                z_array[k] = 0
                i = 0
                # compare str[r+1] with str[r-k+2]
                if string[r] == string[r - k + 1]:
                    match = True
                else:
                    match = False
                while match:
                    i += 1
                    if string[r + i] == string[r - k + 1 + i]:
                        match = True
                    else:
                        match = False

                q = r + i

                z_array[k] = q - k
                l_array[k] = k
                r_array[k] = q

    print('string: ', string)
    print('Z: ', z_array)
    print('l: ', l_array)
    print('r: ', r_array)

    return z_array


# Bad characater shift rule
def calculate_bad_char_shift(pattern):
    """Calculate bad character shift rule."""
    # bad_char = [-1] * len(pattern)
    pass


# Good suffix
def calculate_goodsuffix(pattern):
    """Calculate good suffix values of pattern."""
    m = len(pattern)
    # TODO: Calculate z_suffix
    z_suffix = find_z_array(pattern)
    print(z_suffix)
    # Instantiate goodsuffix array with 0 values.
    goodsuffix = [0] * (m + 1)
    for p in range(0, m-1):
        j = m - z_suffix[p]
        goodsuffix[j] = p


def matches(pat, txt):
    """Simple check if the pat matches against txt."""
    calculate_goodsuffix(pat)
    return True


if __name__ == '__main__':
    # executed directly
    # TODO: Read filenames from arguments.
    print(matches('abc', 'abcd'))
