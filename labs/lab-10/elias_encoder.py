"""
FIT3155 - Lab 10 - Task 1
"""


def encode(numbers_to_encode):
    result = ""
    for number in numbers_to_encode:
        result += encode_single_value(number)

    return len(numbers_to_encode), result


def encode_single_value(number_to_encode):
    # Convert to binary string
    n = convert_to_binary(number_to_encode)

    l_values = []
    l_x = len(n) - 1
    while l_x > 1:
        encoded_l_x = convert_to_binary(l_x)
        # flip first bit of binary string
        encoded_l_x_list = list(encoded_l_x)
        encoded_l_x_list[0] = "0"
        encoded_l_x = "".join(encoded_l_x_list)
        l_values.append(encoded_l_x)
        l_x = len(encoded_l_x) - 1

    # Add value for 1
    l_values.append("0")
    l_values.reverse()

    # Join length values with actual value.
    return "".join(l_values) + n


def convert_to_binary(integer: int):
    return bin(integer)[2:]
