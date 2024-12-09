import numpy as np


def part1(lists):
    left_list, right_list = get_sorted_lists(lists)
    distances = []
    for left, right in zip(left_list, right_list):
        distances.append(abs(left - right))
    print(f"Solution part1: {sum(distances)}")


def part2(lists):
    left_list, right_list = get_sorted_lists(lists)
    unique, counts = np.unique(right_list, return_counts=True)
    similarity_score = []
    for left in left_list:
        count = np.count_nonzero(right_list == left)
        if count != 0:
            similarity_score.append(left * count)

    print(f"Solution part2: {sum(similarity_score)}")


def get_sorted_lists(lists):
    left_list = []
    right_list = []
    for left, right in lists:
        left_list.append(left)
        right_list.append(right)
    return np.sort(left_list), np.sort(right_list)


def main():
    with open("input.txt", "r") as file:
        # Converts file into list
        # strips newline
        # splits each line by whitespace into an array
        # casts each value of the array to integer
        # in lists we have a list of arrays of lists of two integers each
        lists = [list(map(int, line.strip().split())) for line in file]

    part1(lists)
    part2(lists)


if __name__ == "__main__":
    main()
