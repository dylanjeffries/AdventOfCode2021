import sys

if __name__ == "__main__":

    increased_count = 0
    previous_list = []

    with open("input.txt", "r") as f:
        for line in f.readlines():

            current = int(line)
            if len(previous_list) == 3:
                increased_count += sum(previous_list[1:] + [current]) > sum(previous_list)
                previous_list.pop(0)
            previous_list.append(current)

    print(increased_count)
