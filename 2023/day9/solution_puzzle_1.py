from itertools import pairwise

import numpy as np


def get_next_value(sequence):
    sequences = []
    # while sequence is not all zeros, iterate
    while np.any(sequence):
        sequences.append(sequence)
        # create new sequence by extracting pairs of previous one
        sequence = [y - x for x, y in pairwise(sequence)]
    # sum all last elements of all sequences
    return sum([x[-1] for x in sequences])


def main():
    results = []
    with open("input.txt", "r") as file:
        # with open("test_input_puzzle_1.txt", "r") as file:
        report = [list(map(int, line.strip().split())) for line in file]
    # print(report)
    for history in report:
        results.append(get_next_value(history))
    print(f"Puzzle solution {sum(results)}")


if __name__ == "__main__":
    main()
