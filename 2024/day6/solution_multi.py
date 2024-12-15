import numpy as np
from collections import defaultdict
from multiprocessing import Pool, cpu_count

# Directions and guard-related mappings
directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
shift_direction = {"^": ">", ">": "v", "v": "<", "<": "^"}


def is_within_bounds(row, col, shape):
    return 0 <= row < shape[0] and 0 <= col < shape[1]


# Check if all positions are visited twice
def all_positions_visited_twice(visited_positions_tuple):
    visited_positions = defaultdict(int, visited_positions_tuple)
    return all(visits >= 2 for visits in visited_positions.values())


# Precompute valid coordinates
def precompute_valid_coordinates(matrix_shape):
    rows, cols = matrix_shape
    return set((i, j) for i in range(rows) for j in range(cols))


# Get the initial position of the guard
def get_init(matrix):
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] in directions:
                return i, j, matrix[i, j]


# Optimized creates_a_close_loop function
def creates_a_close_loop(matrix, start_row, start_col, start_guard, valid_coordinates):
    matrix[start_row, start_col] = "#"

    row, col, guard = start_row - directions[start_guard][0], start_col - directions[start_guard][1], start_guard
    visited_positions = defaultdict(int)
    visited_positions[(row, col)] += 1

    while True:
        row += directions[guard][0]
        col += directions[guard][1]

        if (row, col) not in valid_coordinates:
            matrix[start_row, start_col] = "."
            return False

        if matrix[row, col] != "#":
            visited_positions[(row, col)] += 1
            if all_positions_visited_twice(tuple(visited_positions.items())):
                matrix[start_row, start_col] = "."
                return True
        else:
            row -= directions[guard][0]
            col -= directions[guard][1]
            guard = shift_direction[guard]

    return False


# Multiprocessing worker for creates_a_close_loop
def worker_task(args):
    matrix, row, col, guard, valid_coordinates = args
    return (row, col) if creates_a_close_loop(matrix, row, col, guard, valid_coordinates) else None


# Patrol function with multiprocessing for part2
def patrol_with_multiprocessing(matrix, init_i, init_j, guard, valid_coordinates):
    positions = set()
    positions_close_loop = set()

    positions.add((init_i, init_j))
    row, col = init_i, init_j

    tasks = []  # Collect tasks for multiprocessing

    while True:
        row += directions[guard][0]
        col += directions[guard][1]

        if (row, col) not in valid_coordinates:
            break
        elif matrix[row, col] != "#":
            positions.add((row, col))

            # Add tasks for multiprocessing
            if (row, col) != (init_i, init_j) and (row, col) not in positions_close_loop:
                tasks.append((matrix.copy(), row, col, guard, valid_coordinates))
        else:
            row -= directions[guard][0]
            col -= directions[guard][1]
            guard = shift_direction[guard]

    # Use multiprocessing to process tasks
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(worker_task, tasks)

    # Filter valid results
    positions_close_loop.update(result for result in results if result is not None)

    return positions, positions_close_loop


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


# Part 2 with multiprocessing
def part2(lines):
    matrix = np.array(lines)
    valid_coordinates = precompute_valid_coordinates(matrix.shape)
    init_i, init_j, guard = get_init(matrix)
    _, positions_close_loop = patrol_with_multiprocessing(matrix, init_i, init_j, guard, valid_coordinates)
    print(f"Solution part2: {len(positions_close_loop)}")


# Main function
def main():
    with open("input.txt", "r") as file:
        lines = [[elem for elem in line.strip()] for line in file]

    part1(lines)  # Unchanged
    part2(lines)


if __name__ == "__main__":
    main()
