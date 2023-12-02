import re


def main():
    digit_regex = re.compile(r"\d")
    results = []
    with open("input.txt", "r") as file:
        for line in file:
            digits = digit_regex.findall(line)
            first_digit = digits[0]
            last_digit = digits[-1]
            calibration_value = int("".join([first_digit, last_digit]))
            results.append(calibration_value)
    print(f"First puzzle solution {sum(results)}")


if __name__ == "__main__":
    main()
