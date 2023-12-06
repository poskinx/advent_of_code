import re


digit_regex = re.compile(r"\d")


def round_is_true(round_filter, game):
    conditions = [
        round_filter["red"] >= game["red"],
        round_filter["green"] >= game["green"],
        round_filter["blue"] >= game["blue"],
    ]
    return all(conditions)


def is_adjacent_to_symbol(input_list, i, j):
    values_to_check = []
    print(f"(i, j) ({i}, {j})")
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            try:
                if i + x < 0 or j + y < 0:
                    continue
                values_to_check.append(input_list[i + x][j + y])
            except IndexError:
                pass
    print(f"Values to check: {values_to_check}")
    for value in values_to_check:
        if value != "." and digit_regex.match(value) is None:
            return True
    return False


def main():
    results = []
    input_list = []
    # with open("test_input_puzzle_1.txt", "r") as file:
    with open("input.txt", "r") as file:
        for line in file:
            input_list.append(line.strip())
    for i in range(len(input_list)):
        row = input_list[i]
        is_part_number = False
        digits = []
        for j in range(len(row)):
            if digit_regex.match(row[j]) is not None:
                print(f"curent value: {row[j]}")
                digits.append(row[j])
                if is_part_number:
                    continue
                else:
                    is_part_number = is_adjacent_to_symbol(input_list, i, j)
            else:
                if is_part_number:
                    results.append(int("".join(digits)))
                is_part_number = False
                digits = []
        if is_part_number:
            results.append(int("".join(digits)))
            is_part_number = False
            digits = []
    print(f"Digits: {results}")
    print(f"First puzzle solution {sum(results)}")


if __name__ == "__main__":
    main()
