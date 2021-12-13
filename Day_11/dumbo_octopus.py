import numpy as np


def increase_adjacent(index, matrix):
    index = np.add(index, (1, 1))
    matrix = np.pad(matrix, pad_width=1, mode="constant", constant_values=0)
    adjacent_indices = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    for adjacent_index in adjacent_indices:
        new_index = tuple(np.add(index, adjacent_index))
        matrix[new_index] += 1

    return matrix[1:-1, 1:-1]


if __name__ == "__main__":

    # Read input
    with open("input.txt", "r") as f:
        octopi = []
        for line in f.readlines():
            octopi.append([int(x) for x in list(line.strip())])

    # Get dimensions of octopi array
    width = len(octopi[0])
    height = len(octopi)

    step = 0
    all_flashed = False
    while not all_flashed:
        # Increment step
        step += 1

        # Create a matrix of matching size filled with 1s for the initial energy level increase
        delta = np.ones((height, width))

        # Set flashed matrix to all 0s, ready to store placements of flashed octopi
        flashed = np.zeros((height, width))

        # While there are changes to be made via the delta matrix
        while np.sum(delta) != 0:
            # Add together the delta matrix and octopi matrix, increasing energy levels accordingly
            octopi += delta
            # Reset the delta matrix to all 0s for adjacent increases to be stored
            delta = np.zeros((height, width))

            # Iterate through every octopus, if the octopus hasn't flashed yet and is due to flash, increase adjacent
            for y, row in enumerate(octopi):
                for x, item in enumerate(row):
                    index = (y, x)

                    if flashed[index] == 0 and item > 9:
                        flashed[index] = 1
                        delta = increase_adjacent(index, delta)

        # For every octopus that flashed this step, set energy level to 0
        for y, row in enumerate(flashed):
            for x, item in enumerate(row):
                if item == 1:
                    octopi[(y, x)] = 0

        # Determine if all the octopi flashed this step
        all_flashed = np.sum(flashed) == flashed.size

    print(f"{step=}")
