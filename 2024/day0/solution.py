def part1(lines):
    count = 0
    print(f"Solution part1: {count}")


def part2(lines):
    count = 0
    print(f"Solution part2: {count}")


def main():
    with open("input.txt", "r") as file:
        # Converts file into list
        # strips newline for each line
        lines = [line.strip() for line in file]

    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
