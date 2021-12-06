import numpy as np


def is_winning_line(row, called_numbers):
    return all(x in called_numbers for x in row)


def has_winning_line(board, called_numbers):
    return any(is_winning_line(row, called_numbers) for row in board)


def find_winning_board(boards, called_numbers):
    iteration_winners = []
    for board in boards:
        has_winning_row = has_winning_line(board, called_numbers)
        transposed_board = np.array(board).T.tolist()
        has_winning_col = has_winning_line(transposed_board, called_numbers)

        if has_winning_row or has_winning_col:
            iteration_winners.append(board)
    return iteration_winners


def calculate_unmarked_sum(board, called_numbers):
    flat_board = np.array(board).flatten()
    unmarked = np.setdiff1d(flat_board, np.array(called_numbers)).astype(int)
    return sum(unmarked)


if __name__ == "__main__":

    with open("input.txt", "r") as f:
        # Extract the call order from the first line
        call_order = f.readline().strip().split(",")
        # Extract each board and store as 2d arrays
        boards = []
        for line in f.readlines():
            if line == "\n":
                boards.append([])
            else:
                boards[-1].append(line.split())

    called_numbers = []
    final_winning_board = None
    final_called_numbers = []
    for i, v in enumerate(call_order):
        called_numbers = call_order[:i+1]
        iteration_winners = find_winning_board(boards, called_numbers)

        for winning_board in iteration_winners:
            final_winning_board = winning_board
            final_called_numbers = called_numbers
            boards.remove(winning_board)

    last_called_number = int(final_called_numbers[-1])
    unmarked_sum = calculate_unmarked_sum(final_winning_board, final_called_numbers)
    score = last_called_number * unmarked_sum
    print(f"{score=}")
