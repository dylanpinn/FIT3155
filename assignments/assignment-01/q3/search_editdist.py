"""Search Edit Distance"""

from q3.z_algorithm import find_z_array


def reverse_string(string):
    """Reverse string using a slice."""
    return string[::-1]


def search(pat, txt, index_offset=1):
    full_text = pat + '$' + txt
    reverse_full_txt = reverse_string(pat) + '$' + reverse_string(txt)
    z_array = find_z_array(full_text)
    rev_z_array = find_z_array(reverse_full_txt)
    result = []
    m = len(pat)
    n = len(txt)

    for i in range(n):
        j = i + m + 1  # current index in z_array
        k = m + n - i

        # Matches with no edit distance
        if z_array[j] == m:
            result.append((i + index_offset, 0))

        # Insert
        # - Insert at start
        if rev_z_array[k - (m - 1) + 1] == m - 1:
            result.append((i + index_offset, 1))

        print('find insert')

        # Substitute

        # Delete

    return result
