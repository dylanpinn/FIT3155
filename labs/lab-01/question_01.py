"""Gusfield Z-Algorithm

"""


def matches(pattern, txt):
    """Does pattern exist in text."""
    result = find_matches(pattern, txt)
    if result:
        return True
    return False


def find_matches(pattern, txt):
    """Find matches using Gusfield's algorithm."""
    string = pattern + "$" + txt
    result = []
    z_values = z_array(string)
    for i in z_values:
        if i == len(pattern):
            result.append(i - len(pattern) - 1)

    return result


def finding_match(string, right, left):
    """See if we should keep moving through z_box."""
    return right < len(string) and string[right] == string[right - left]


def z_array(string):
    """Implement Gusfield's Z-algorithm to generate Z-array."""
    z_array = [None] * len(string)
    left, right = 0, 0

    for k in range(1, len(string)):
        if k > right:
            left = right = k
            while finding_match(string, right, left):
                right += 1
            z_array[k] = right - left
            right -= 1
        else:
            kl = k - left
            if z_array[kl] < right - k + 1:
                z_array[k] = z_array[kl]
            else:
                left = k
                while finding_match(string, right, left):
                    right += 1
                z_array[k] = right - left
                right -= 1

    return z_array


if __name__ == '__main__':
    find_matches('aab', 'aabaabcaxaabaabcy')
