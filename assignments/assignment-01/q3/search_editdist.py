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

    for i in range(m + 1, len(z_array)):
        # j = i + m + 1  # current index in z_array
        k = len(z_array) - i + m

        iteration = i - m - 1

        # Matches with no edit distance
        if z_array[i] == m:
            result.append((i + index_offset - (m + 1), 0))

        # Substitute
        # - Substitute at start
        elif rev_z_array[k - m + 1] == m - 1:
            result.append((i + index_offset - (m + 1), 1))

        # - Substitute at middle
        elif z_array[i] + rev_z_array[k - m + 1] == m - 1:
            result.append((i + index_offset - (m + 1), 1))

        # - Substitute at end
        elif z_array[i] == m - 1:
            result.append((i + index_offset - (m + 1), 1))

        # Insert
        # - Insert at start
        elif rev_z_array[k - m + 2] == m - 1:
            result.append((i + index_offset - (m + 1), 1))

        # - Insert in middle
        elif z_array[i] + rev_z_array[k - m + 2] == m - 1:
            result.append((i + index_offset - (m + 1), 1))

        # - Insert at end
        elif z_array[i] == m - 1:
            result.append((i + index_offset - (m + 1), 1))

        # Delete - in the middle
        elif z_array[i] + rev_z_array[k - m] == m:
            if rev_z_array[k - m] != m:
                result.append((i + index_offset - (m + 1), 1))
        else:
            print('here')

    return result
