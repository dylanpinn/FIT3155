"""Calculate Z-Algorithm using Gusfield's algorithm"""


def find_match(string, right, left):
    """See if we should keep moving through z_box."""
    return right < len(string) and string[right] == string[right - left]


def z_array(string: str, index_to_stop: int):
    """Calculate Z-Array using Gusfield's Algorithm.

    Modified to optionally stop at an index.
    """
    z_array = [None] * len(string)
    left, right = 0, 0

    for k in range(1, len(string)):
        if k >= index_to_stop:
            break
        if k > right:
            left = right = k
            while find_match(string, right, left):
                right += 1
            z_array[k] = right - left
            right -= 1
        else:
            kl = k - left
            if z_array[kl] < right - k + 1:
                z_array[k] = z_array[kl]
            else:
                left = k
                while find_match(string, right, left):
                    right += 1
                z_array[k] = right - left
                right -= 1

    return z_array
