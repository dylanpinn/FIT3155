# Gusfield Z-Algorithm

def gusfield(pattern, string):
    # 3 cases
    # 1. k > r
    # 2. k = r
    # 3. k < r

    # pattern = "aab"
    string = "aabaabcaxaabaabcy"
    # concat_string = pattern + "$" + string
    z_array = [None] * len(string)
    r_array = [None] * len(string)
    l_array = [None] * len(string)

    # Base Case

    # match string[2...] with string[1...] until mismatch is found

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


        # k = 2
        # for k in range(len(string)):
        #   # check case 1
        #   if k > r:
        #     # case 1
        #     # compare strings str[k...q-1] with str[1...q-k] until mismatch
        #     break;
        #   elif k == r:
        #     # case 2
        #     break;
        #   elif k < r:
        #     # case 3
        #     break;
        #   else:
        #     # blow up
        #     raise Exception('error')


    print('string: ', string)
    print('Z: ', z_array)
    print('l: ', l_array)
    print('r: ', r_array)

gusfield('aab', 'aabaabcaxaabaabcy')
