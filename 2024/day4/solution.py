import numpy as np


keyword = "XMAS"


def part1(lines):
    matrix = np.array(lines)
    count = 0
    for column, row in np.ndindex(matrix.shape):
        if matrix[column, row] == "X":
            count += count_xmas_word(matrix, row, column)
    print(f"Solution part1: {count}")


def count_xmas_word(matrix, row, column):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    count = 0
    for dx, dy in directions:
        if search_word(matrix, row, column, dx, dy, keyword):
            count += 1
    return count


def search_word(matrix, row, column, dx, dy, word):
    for i, char in enumerate(word):
        x, y = row + i * dx, column + i * dy
        if x < 0 or y < 0 or x >= matrix.shape[1] or y >= matrix.shape[0] or matrix[y, x] != char:
            return False
    return True


def part2(lines):
    matrix = np.array(lines)
    rows, cols = matrix.shape
    count = 0

    # Iterate over all valid 3x3 sub-matrices
    for i in range(rows - 2):
        for j in range(cols - 2):
            # Extract the 3x3 sub-matrix
            sub_matrix = matrix[i : i + 3, j : j + 3]

            # Check if it matches the "X-MAS" pattern
            if is_x_mas_pattern(sub_matrix):
                count += 1
    print(f"Solution part2: {count}")


# Define the target "X-MAS" pattern
def is_x_mas_pattern(sub_matrix):
    """
    Check if the 3x3 sub-matrix matches any valid "X-MAS" pattern.
    """
    # Extract the rows
    top_row = sub_matrix[0]
    middle_row = sub_matrix[1]
    bottom_row = sub_matrix[2]

    # Middle row must have 'A' in the center
    if middle_row[1] != "A":
        return False

    # Check for valid top and bottom rows
    def is_valid_row(top_row, bottom_row):
        return (
            (top_row[0] == "M" and top_row[2] == "M" and bottom_row[0] == "S" and bottom_row[2] == "S")
            or (  # Matches M.M//S.S
                top_row[0] == "S" and top_row[2] == "S" and bottom_row[0] == "M" and bottom_row[2] == "M"
            )
            or (  # Matches S.S/M.M
                top_row[0] == "M" and top_row[2] == "S" and bottom_row[0] == "M" and bottom_row[2] == "S"
            )
            or (  # Matches M.S/M.S
                top_row[0] == "S" and top_row[2] == "M" and bottom_row[0] == "S" and bottom_row[2] == "M"
            )  # Matches S.M/S.M
        )

    # Check if top and bottom rows are valid
    return is_valid_row(top_row, bottom_row)


def main():
    with open("input.txt", "r") as file:
        # Converts file into list
        # strips newline for each line
        lines = [[letter for letter in line.strip()] for line in file]

    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
