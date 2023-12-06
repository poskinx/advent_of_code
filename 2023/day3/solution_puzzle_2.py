import re


digit_regex = re.compile(r"\d")
all_gears = []
gears = []


def round_is_true(round_filter, game):
    conditions = [
        round_filter["red"] >= game["red"],
        round_filter["green"] >= game["green"],
        round_filter["blue"] >= game["blue"],
    ]
    return all(conditions)


def add_gear(input_list, i, j):
    numbers = []
    count_adjacents = 0
    # print(f"(i, j) ({i}, {j})")
    for x in [-1, 0, 1]:
        previous_was_number = False
        for y in [-1, 0, 1]:
            if i + x < 0 or j + y < 0:
                continue
            value = input_list[i + x][j + y]
            # print(f"(i, y): ({i+x}, {j+y}), value: {value}")
            if digit_regex.match(value) is not None:
                if not previous_was_number:
                    count_adjacents += 1
                    # print(f"count_adjacents: {count_adjacents}")
                    previous_was_number = True
                    numbers.append(get_number(input_list[i + x], j + y))
                if count_adjacents > 2:
                    return
            else:
                previous_was_number = False
    # print(f"Numbers: {numbers}")
    if len(numbers) == 2:
        all_gears.append(numbers)
        gears.append(numbers[0] * numbers[1])


def get_number(row, j):
    left_nums = []
    right_nums = []
    digits = []
    right = left = True
    x = y = 0
    while right or left:
        x += 1
        y -= 1
        try:
            if right and digit_regex.match(row[j + x]) is not None:
                right_nums.append(row[j + x])
            else:
                right = False
        except IndexError:
            right = False
        try:
            if left and digit_regex.match(row[j + y]) is not None:
                left_nums.append(row[j + y])
            else:
                left = False
        except IndexError:
            left = False
    digits.extend(n for n in reversed(left_nums))
    digits.append(row[j])
    digits.extend(right_nums)
    # print(f"Digits: {''.join(digits)}")
    return int("".join(digits))


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
            if row[j] == "*":
                # print(f"curent value: {row[j]}")
                digits.append(row[j])
                if is_part_number:
                    continue
                else:
                    is_part_number = add_gear(input_list, i, j)
            else:
                if is_part_number:
                    results.append(int("".join(digits)))
                is_part_number = False
                digits = []
        if is_part_number:
            results.append(int("".join(digits)))
            is_part_number = False
            digits = []
    print(f"Digits: {all_gears}")
    print(f"First puzzle solution {sum(gears)}")


if __name__ == "__main__":
    main()
