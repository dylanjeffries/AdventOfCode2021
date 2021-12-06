if __name__ == "__main__":

    # Read input
    ages = [0] * 9
    with open("input.txt", "r") as f:
        for x in f.readline().split(","):
            ages[int(x)] += 1

    for i in range(1, 257):
        # Save 0 ages
        zero = ages[0]

        # Shift ages 1 to 8 to the left
        for j in range(8):
            ages[j] = ages[j+1]

        # Add saved 0 ages to 6 ages
        ages[6] += zero

        # Set 8 ages to saved 0 ages
        ages[8] = zero

    print(ages)
    print(sum(ages))
