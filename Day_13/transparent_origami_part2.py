import numpy as np


if __name__ == "__main__":

    dots = []
    folds = []
    width = 0
    height = 0

    # Read input
    with open("input.txt", "r") as f:
        for line in f.readlines():
            stripped_line = line.strip()

            if "," in stripped_line:
                x, y = [int(i) for i in stripped_line.split(",")]
                width = max(width, x + 1)
                height = max(height, y + 1)
                dots.append(tuple([y, x]))
            elif "y=" in stripped_line:
                folds.append((0, int(stripped_line.split("=")[1])))
            elif "x=" in stripped_line:
                folds.append(((int(stripped_line.split("=")[1])), 0))

    # Assemble matrix with dots represented as True
    matrix = np.full((height, width), False, dtype=bool)
    for dot in dots:
        matrix[dot] = True

    # For each fold, split the matrix into two parts, flip the secondary part, and overlap it with the primary part
    for fold in folds:
        # Set boundaries for the two parts based on the axis of the fold line
        primary_y = fold[1] if fold[0] == 0 else height
        primary_x = width if fold[0] == 0 else fold[0]
        secondary_y = fold[1] + 1 if fold[0] == 0 else height
        secondary_x = width if fold[0] == 0 else fold[0] + 1

        if fold[0] == 0:
            primary = matrix[:fold[1], :width]
            secondary = np.flip(matrix[fold[1] + 1:, :width], axis=0)
        else:
            primary = matrix[:height, :fold[0]]
            secondary = np.flip(matrix[:height, fold[0] + 1:], axis=1)

        matrix = np.logical_or(primary, secondary)

    # Print matrix as dots (hash) and non-dots (full stop)
    for row in matrix:
        print("".join(["#" if i else "." for i in row]))
