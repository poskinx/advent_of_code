import re


def main():
    digit_regex = re.compile(r"\d")
    pattern_repl_tuples = [
        ("one", "o1e"),
        ("two", "t2o"),
        ("three", "t3e"),
        ("four", "4"),
        ("five", "f5e"),
        ("six", "s6x"),
        ("seven", "s7n"),
        ("eight", "e8t"),
        ("nine", "n9e"),
    ]
    results = []
    # with open("test_input_puzzle_2.txt", 'r') as file:
    with open("input.txt", "r") as file:
        for line in file:
            for pattern, repl in pattern_repl_tuples:
                line = re.sub(pattern, repl, line)
            digits = digit_regex.findall(line)
            first_digit = digits[0]
            last_digit = digits[-1]
            calibration_value = int("".join([first_digit, last_digit]))
            results.append(calibration_value)
    # print(results)
    print(f"First puzzle solution {sum(results)}")


if __name__ == "__main__":
    main()
