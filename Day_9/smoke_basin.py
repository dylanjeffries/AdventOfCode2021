import numpy as np


def visit(index, delta, visited, matrix):
    new_index = (index[0] + delta[0], index[1] + delta[1])
    if new_index not in visited:
        visited = radiate(new_index, visited, matrix)
    return visited


def radiate(index, visited, matrix):
    # Base
    if matrix[index] == 9.0:
        return visited

    # Mark current index as visited and travel to adjacent cells that haven't been visited yet
    visited.append(index)
    visited = visit(index, (0, -1), visited, matrix)
    visited = visit(index, (1, 0), visited, matrix)
    visited = visit(index, (0, 1), visited, matrix)
    visited = visit(index, (-1, 0), visited, matrix)

    return visited


if __name__ == "__main__":
    # Load matrix from file using a column width of 1
    matrix = np.genfromtxt("input.txt", delimiter=1)

    # Apply a border of 9s to the matrix in order to give corners and edges an adjacent element in all directions
    padded_matrix = np.pad(matrix, pad_width=1, mode="constant", constant_values=9)

    # Create a new matrix for each adjacent comparison
    north_matrix = padded_matrix < np.roll(padded_matrix, 1, 0)
    east_matrix = padded_matrix < np.roll(padded_matrix, -1, 1)
    south_matrix = padded_matrix < np.roll(padded_matrix, -1, 0)
    west_matrix = padded_matrix < np.roll(padded_matrix, 1, 1)

    # Use the AND operator to get if each element is lower than all adjacent elements
    low_points_matrix = (north_matrix & east_matrix & south_matrix & west_matrix)
    # Use the boolean low points matrix as a mask to extract the values of the elements that were True
    low_values_matrix = padded_matrix[low_points_matrix]
    # Calculate risk level by summing the low point values and adding 1 for each value found
    risk_level = sum(low_values_matrix) + len(low_values_matrix)
    # print(f"{risk_level=}")

    # Get list of low point coords as tuples
    y, x = low_points_matrix.nonzero()
    low_points_tuples = list(zip(y, x))

    # From every low point, radiate outwards counting the adjacent elements that are part of the same basin
    basins = []
    for low_point in low_points_tuples:
        basins.append(len(radiate(low_point, [], padded_matrix)))

    # Find the three largest basin sizes and calculate the answer
    basins.sort(reverse=True)
    answer = np.prod(basins[:3])
    print(f"{answer=}")
