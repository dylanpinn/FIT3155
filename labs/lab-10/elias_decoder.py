"""
FIT3155 - Lab 10 - Task 2
"""


def decode_single_value(codeword):
    read_len = convert_to_decimal("1")
    pos = 0
    while True:
        component = codeword[pos : pos + read_len]
        if component[0] == "1":
            return convert_to_decimal(component)
        else:
            # flip first bit of binary string
            encoded_list = list(component)
            encoded_list[0] = "1"
            component = "".join(encoded_list)
            component_as_decimal = convert_to_decimal(component)
            pos = pos + read_len
            read_len = component_as_decimal + 1


def convert_to_decimal(binary_string: str):
    return int(binary_string, 2)
