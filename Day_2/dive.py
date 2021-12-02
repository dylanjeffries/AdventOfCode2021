if __name__ == "__main__":

    # Origin at top left
    x, y = 0, 0
    aim = 0

    with open("input.txt", "r") as f:
        for line in f.readlines():

            command, units = line.split(" ")
            if command == "forward":
                x += int(units)
                y += int(units) * aim
            elif command == "up":
                aim -= int(units)
            elif command == "down":
                aim += int(units)

    print(x, y)
    print(x * y)
