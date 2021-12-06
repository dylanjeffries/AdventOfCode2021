def polarity(number):
    if number < 0:
        return -1
    return 1


def show_grid(grid):
    for row in grid:
        print("".join([str(x) for x in row]))


if __name__ == "__main__":

    # Read input and determine dimensions of the grid
    lines = []
    dimensions = (0, 0)
    with open("input.txt", "r") as f:
        for f_line in f.readlines():
            line = f_line.replace(" -> ", ",").split(",")
            line = [int(x) for x in line]
            lines.append(line)
            dimensions = (max(dimensions[0], line[0], line[2]), max(dimensions[1], line[1], line[3]))

    # Create default grid
    grid = [[0] * (dimensions[0] + 1) for y in range(dimensions[1] + 1)]

    # Process each line on the grid
    for line in lines:
        # Determine x and y coords of all points on the line
        polarity_x = polarity(line[2] - line[0])
        points_x = list(range(line[0], line[2]+polarity_x, polarity_x))
        polarity_y = polarity(line[3] - line[1])
        points_y = list(range(line[1], line[3]+polarity_y, polarity_y))
        # Only process non-diagonal lines
        if len(points_x) == 1 or len(points_y) == 1 or len(points_x) == len(points_y):
            # Stretch the coords list thats the shortest
            if len(points_x) > len(points_y):
                points_y = points_y * len(points_x)
            else:
                points_x = points_x * len(points_y)
            # Create a list of x, y coords for all points on the line
            points = [[a, b] for a, b in zip(points_x, points_y)]
            # For every point, increase grid point value by 1
            for x, y in points:
                grid[y][x] += 1

    show_grid(grid)

    # Count number of times a 2 or more occurs in the grid
    occurences = 0
    for row in grid:
        occurences += sum([1 for x in row if x >= 2])
    print(f"{occurences=}")






