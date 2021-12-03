import math

import numpy as np


def round_with_favour(number, round_up):
    # Ends in 0.5 and you want to round up
    if (number - 0.5).is_integer() and round_up:
        return math.ceil(number)
    # Else
    return round(number)


def common_binaries(binaries, round_up):
    sum_list = None
    for binary in binaries:
        binary_list = [int(x) for x in list(binary)]
        sum_list = binary_list if sum_list is None else np.add(sum_list, binary_list)
    binaries_length = len(binaries)
    most_common = "".join([str(round_with_favour(x / binaries_length, round_up)) for x in sum_list])
    all_ones = '1' * len(most_common)
    least_common = f"{int(most_common, 2) ^ int(all_ones, 2):0{len(most_common)}b}"

    return most_common, least_common


if __name__ == "__main__":

    with open("input.txt", "r") as f:
        input_binaries = [line.replace("\n", "") for line in f.readlines()]

    input_most_common, input_least_common = common_binaries(input_binaries, False)
    power_consumption = int(input_most_common, 2) * int(input_least_common, 2)
    print(f"{power_consumption=}")

    oxygen_list = input_binaries
    pointer = 0
    while len(oxygen_list) > 1:
        oxygen_most_common, oxygen_least_common = common_binaries(oxygen_list, True)
        oxygen_list = list(filter(lambda x: x[pointer] == oxygen_most_common[pointer], oxygen_list))
        pointer += 1

    co2_list = input_binaries
    pointer = 0
    while len(co2_list) > 1:
        co2_most_common, co2_least_common = common_binaries(co2_list, True)
        co2_list = list(filter(lambda x: x[pointer] == co2_least_common[pointer], co2_list))
        pointer += 1

    life_support = int(oxygen_list[0], 2) * int(co2_list[0], 2)
    print(f"{life_support=}")
