"""Gusfield Z-Algorithm

"""

def find_match(pattern, txt):
    """Find match using Gusfield's algorithm."""
    # TODO: Work with pattern and string arguments.
    string = pattern + "$" + txt
    z_values = gusfield(string)
    print(z_values)
    for i in z_values:
        if i == len(pattern):
            return True
        else:
            return False


def base_case(string):
    z_array = [None] * len(string)
    r_array = [None] * len(string)
    l_array = [None] * len(string)
    # compare l-r string[1] == string[0] until mismatch is found
    match = True
    z_index = 1
    z_array[z_index] = 0
    i = 1
    print(len(string))
    while match and i < len(string):
        print(i, i-z_index)
        if string[i] == string[i - z_index]:
            match = True
            z_array[z_index] += 1
        else:
            match = False
        i += 1
    if z_array[z_index] > 0:
        r_array[z_index] = z_array[z_index]
        l_array[z_index] = 1
    else:
        r_array[z_index], l_array[z_index] = 0, 0
    print(z_array)

    return z_array, r_array, l_array


def gusfield(string):
    # TODO: Remove duplicated code.
    z_array, r_array, l_array = base_case(string)

    for k in range(2, len(string)):
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


if __name__ == '__main__':
    find_match('aab', 'aabaabcaxaabaabcy')
