import numpy as np
from collections import defaultdict

directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
shift_direction = {"^": ">", ">": "v", "v": "<", "<": "^"}


def get_init(matrix):
    # Accessing by indices
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] in directions:
                return i, j, matrix[i, j]


def is_within_bounds(row, col, shape):
    return 0 <= row < shape[0] and 0 <= col < shape[1]


def all_positions_visited_twice(visited_positions):
    if all(visits >= 2 for visits in visited_positions.values()):
        return True


def creates_a_close_loop(matrix, start_row, start_col, start_guard):
    # Create a copy of the matrix to simulate adding the obstacle
    simulated_matrix = matrix.copy()
    simulated_matrix[start_row, start_col] = "#"  # Add obstruction

    # Go 1 step back because now there is an obstacle in start position
    row = start_row - directions[start_guard][0]
    col = start_col - directions[start_guard][1]
    guard = start_guard

    # Track visits to each position
    visited_positions = defaultdict(int)
    visited_positions[",".join([str(row), str(col)])] += 1

    rows = len(matrix)
    cols = len(matrix[0])
    safety_limit = rows * cols * 2
    safety_count = 0
    while True:
        # Move forward
        row += directions[guard][0]
        col += directions[guard][1]
        safety_count += 1
        if safety_count > safety_limit:
            # no close loops
            break

        # Check if out of bounds
        if not is_within_bounds(row, col, simulated_matrix.shape):
            break
        #
        elif simulated_matrix[row, col] != "#":
            visited_positions[",".join([str(row), str(col)])] += 1
            if all_positions_visited_twice(visited_positions):
                return True
        else:
            row -= directions[guard][0]
            col -= directions[guard][1]
            guard = shift_direction[guard]
    return False


def patrol(matrix, init_i, init_j, guard, part2=False):
    positions = set()
    positions_close_loop = set()
    positions.add((init_i, init_j))
    row = init_i
    col = init_j
    while True:
        row += directions[guard][0]
        col += directions[guard][1]
        if not is_within_bounds(row, col, matrix.shape):
            # print((row, col), matrix.shape)
            break
        elif matrix[row, col] != "#":
            positions.add((row, col))
            # it is a close loop? -> count +1
            # Exclude starting position
            if part2 and (row, col) != (init_i, init_j) and (row, col) not in positions_close_loop:
                if creates_a_close_loop(matrix, row, col, guard):
                    positions_close_loop.add((row, col))
        else:
            row -= directions[guard][0]
            col -= directions[guard][1]
            guard = shift_direction[guard]
        # print(guard, (row, col), positions)
    return positions, positions_close_loop


def part1(lines):
    matrix = np.array(lines)
    init_i, init_j, guard = get_init(matrix)
    positions, _ = patrol(matrix, init_i, init_j, guard)
    print(f"Solution part1: {len(positions)}")


def part2(lines):
    matrix = np.array(lines)
    init_i, init_j, guard = get_init(matrix)
    _, positions_close_loop = patrol(matrix, init_i, init_j, guard, part2=True)
    print(f"Solution part2: {len(positions_close_loop)}")


def main():
    with open("input.txt", "r") as file:
        # Converts file into list
        # strips newline for each line
        lines = [[elem for elem in line.strip()] for line in file]

    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
