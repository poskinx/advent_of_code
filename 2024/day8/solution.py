from collections import defaultdict
import numpy as np


def is_within_bounds(antinode, shape):
    return 0 <= antinode[0] < shape[0] and 0 <= antinode[1] < shape[1]


def get_frequencies(matrix):
    frequencies = defaultdict(set)
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            elem = matrix[row, col]
            if elem != ".":
                frequencies[elem].add((row, col))
    return frequencies


def get_position_pairs(frequencies):
    position_pairs = []
    for frequency, positions in frequencies.items():
        pairs = [(x, y) for x in positions for y in positions if x != y]
        position_pairs.extend(pairs)
    return position_pairs


def get_unique_antinodes(position_pairs, shape):
    unique_antinodes = set()
    for pos1, pos2 in position_pairs:
        diff = tuple(a - b for a, b in zip(pos1, pos2))
        antinode_1 = tuple(a + b for a, b in zip(pos1, diff))
        if is_within_bounds(antinode_1, shape):
            unique_antinodes.add(antinode_1)
        antinode_2 = tuple(a - b for a, b in zip(pos2, diff))
        if is_within_bounds(antinode_2, shape):
            unique_antinodes.add(antinode_2)
    return unique_antinodes


def get_harmonic_antinodes(position_pairs, shape):
    unique_antinodes = set()
    for pos1, pos2 in position_pairs:
        diff = tuple(a - b for a, b in zip(pos1, pos2))
        antinode_1 = tuple(a + b for a, b in zip(pos1, diff))
        unique_antinodes.add(pos1)
        while True:
            if is_within_bounds(antinode_1, shape):
                unique_antinodes.add(antinode_1)
            else:
                break
            antinode_1 = tuple(a + b for a, b in zip(antinode_1, diff))
        unique_antinodes.add(pos2)
        antinode_2 = tuple(a - b for a, b in zip(pos2, diff))
        while True:
            if is_within_bounds(antinode_2, shape):
                unique_antinodes.add(antinode_2)
            else:
                break
            antinode_2 = tuple(a - b for a, b in zip(antinode_2, diff))
    return unique_antinodes


def part1(lines):
    matrix = np.array(lines)
    frequencies = get_frequencies(matrix)
    position_pairs = get_position_pairs(frequencies)
    unique_antinodes = get_unique_antinodes(position_pairs, matrix.shape)
    print(f"Solution part1: {len(unique_antinodes)}")


def part2(lines):
    matrix = np.array(lines)
    frequencies = get_frequencies(matrix)
    position_pairs = get_position_pairs(frequencies)
    unique_antinodes = get_harmonic_antinodes(position_pairs, matrix.shape)
    print(f"Solution part2: {len(unique_antinodes)}")


def main():
    with open("input.txt", "r") as file:
        # Converts file into list
        # strips newline for each line
        lines = [[elem for elem in line.strip()] for line in file]

    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
