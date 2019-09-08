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
        # k = m + n - i

        iteration = i - m - 1

        # Matches with no edit distance
        if z_array[i] == m:
            result.append((i + index_offset - (m + 1), 0))
            break

        # Substitute
        # - Substitute at start
        if rev_z_array[i] == m - 1:
            result.append((i + index_offset - (m + 1), 1))
            break

        # - Substitute at middle
        if z_array[i] + rev_z_array[len(z_array) - (i - m + 1) - (m - 1) + 1] == m - 1:
            result.append((i + index_offset - (m + 1), 1))
            break

        # - Substitute at end
        if rev_z_array[i] == m - 1:
            result.append((i + index_offset - (m + 1), 1))
            break

        # Insert
        # - Insert at start
        if rev_z_array[len(z_array) - (i - m + 1) - 1] == m - 1:
            result.append((i + index_offset - (m + 1), 1))
            break

        # # - Insert in middle
        # if z_array[j] + rev_z_array[j + (m - 1) - 1] == m - 1:
        #     result.append((i + index_offset, 1))
        #     break

        # - Insert at end
        if z_array[i] == m - 1:
            result.append((i + index_offset - (m + 1), 1))
            break

        print('find insert')

        # Delete

    return result
