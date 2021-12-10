import math


PAIRS = {")": {"opener": "(", "error": 3},
         "]": {"opener": "[", "error": 57},
         "}": {"opener": "{", "error": 1197},
         ">": {"opener": "<", "error": 25137}}

COMPLETE_SCORES = {"(": 1, "[": 2, "{": 3, "<": 4}


def line_check(line):
    # Iterate through the line, adding opening chars to the stack and popping them if the closing char is detected
    # If a closing char doesn't match the current top opening char in the stack, the line is corrupt
    stack = []
    for c in line:
        if c in PAIRS:
            opener = PAIRS[c]["opener"]
            if stack.pop() != opener:
                return c, None
        else:
            stack.append(c)

    # If the stack isn't empty after the corrupt check, the line is incomplete
    # Use the unused opening chars to calculate the completion score
    if stack:
        stack.reverse()
        complete = 0
        for c in stack:
            complete *= 5
            complete += COMPLETE_SCORES[c]
        return None, complete

    return None, None


if __name__ == "__main__":

    # Read input
    with open("input.txt", "r") as f:

        illegal_chars = []
        complete_scores = []

        for line in f.readlines():

            illegal, complete = line_check(line.strip())
            if illegal is not None:
                illegal_chars.append(illegal)
            if complete is not None:
                complete_scores.append(complete)

    # Calculate error score
    error_score = sum([PAIRS[x]["error"] for x in illegal_chars])
    print(f"{error_score=}")

    # Sort complete scores, calculate the index of the middle value, and find the middle score
    complete_scores.sort()
    print(complete_scores)
    middle_index = math.floor(len(complete_scores) / 2)
    middle_score = complete_scores[middle_index]
    print(f"{middle_score=}")




