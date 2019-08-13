# Gusfield Z-Algorithm


def gusfield(pattern, string):
    # TODO: Add tests.
    # TODO: Meet PEP8
    # TODO: Meet PEP256
    # TODO: Remove duplicated code.
    # TODO: Work with pattern and string arguments.

    # pattern = "aab"
    string = "aabaabcaxaabaabcy"
    # concat_string = pattern + "$" + string
    z_array = [None] * len(string)
    r_array = [None] * len(string)
    l_array = [None] * len(string)

    # Base Case

    # match string[1...] with string[0...] until mismatch is found

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

gusfield('aab', 'aabaabcaxaabaabcy')
