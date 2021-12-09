def alpha(string):
    return "".join(sorted(string))


if __name__ == "__main__":

    # Read input
    with open("input.txt", "r") as f:
        outputs_sum = 0
        for line in f.readlines():

            patterns, outputs = [x.strip().split(" ") for x in line.split(" | ")]

            # Extract patterns with unique lengths that match the digits 1, 7, 4, and 8
            # Also, place patterns with a length of 5 or 6 in the corresponding array for later use
            digit_patterns = {}
            one_pattern = ""
            four_pattern = ""
            five_lengths = []
            six_lengths = []
            for p in patterns:
                p_len = len(p)
                if p_len == 2:
                    digit_patterns[alpha(p)] = "1"
                    one_pattern = alpha(p)
                elif p_len == 3:
                    digit_patterns[alpha(p)] = "7"
                elif p_len == 4:
                    digit_patterns[alpha(p)] = "4"
                    four_pattern = alpha(p)
                elif p_len == 7:
                    digit_patterns[alpha(p)] = "8"
                elif p_len == 5:
                    five_lengths.append(p)
                elif p_len == 6:
                    six_lengths.append(p)

            # For each pattern of length 5, compare the pattern to those of digits 1 and 4
            # Use the sum of letters missing that are present in 1 and 4 to determine the digit of each pattern
            for p in five_lengths:
                p_sum = sum([1 for letter in one_pattern if letter not in p])
                p_sum += sum([1 for letter in four_pattern if letter not in p])
                if p_sum == 1:
                    digit_patterns[alpha(p)] = "3"
                elif p_sum == 2:
                    digit_patterns[alpha(p)] = "5"
                elif p_sum == 3:
                    digit_patterns[alpha(p)] = "2"

            # For each pattern of length 6, compare the pattern to those of digits 1 and 4
            # Use the sum of letters missing that are present in 1 and 4 to determine the digit of each pattern
            for p in six_lengths:
                p_sum = sum([1 for letter in one_pattern if letter not in p])
                p_sum += sum([1 for letter in four_pattern if letter not in p])
                if p_sum == 0:
                    digit_patterns[alpha(p)] = "9"
                elif p_sum == 1:
                    digit_patterns[alpha(p)] = "0"
                elif p_sum == 2:
                    digit_patterns[alpha(p)] = "6"

            outputs_digits = [digit_patterns[alpha(p)] for p in outputs]
            outputs_sum += int("".join(outputs_digits))

        print(outputs_sum)
