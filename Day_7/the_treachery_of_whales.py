import statistics
import math


def triangular_number(number):
    return (number * (number + 1)) / 2


if __name__ == "__main__":

    # Read input
    with open("input.txt", "r") as f:
        positions = [int(x) for x in f.readline().split(",")]

    median_position = statistics.median(positions)
    mean_position = statistics.mean(positions)
    mean_lower = math.floor(mean_position)
    mean_upper = math.ceil(mean_position)

    fuel_lower = 0
    fuel_upper = 0
    for position in positions:
        fuel_lower += triangular_number(abs(position - mean_lower))
        fuel_upper += triangular_number(abs(position - mean_upper))

    print(mean_lower, fuel_lower)
    print(mean_upper, fuel_upper)
