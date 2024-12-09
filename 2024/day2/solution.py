def part1(reports):
    safe_reports = []
    for levels in reports:
        # print(levels, report_is_safe(levels))
        if report_is_safe(levels):
            safe_reports.append(1)
        else:
            safe_reports.append(0)

    print(f"Solution part1: {sum(safe_reports)}")


def part2(reports):
    safe_reports = []
    for levels in reports:
        # print(levels, report_is_safe(levels))
        if report_is_safe(levels):
            safe_reports.append(1)
        else:
            safe_w_removing = False
            for index, _ in enumerate(levels):
                """
                >>> levels = [7, 6, 4, 2, 1]
                >>> for index, _ in enumerate(levels):
                    ...     print(levels[:index] + levels[index + 1:])
                    ...
                    [6, 4, 2, 1]
                    [7, 4, 2, 1]
                    [7, 6, 2, 1]
                    [7, 6, 4, 1]
                    [7, 6, 4, 2]

                """
                levels_sliced = levels[:index] + levels[index + 1 :]
                if report_is_safe(levels_sliced):
                    safe_w_removing = True
                    break
            if safe_w_removing:
                safe_reports.append(1)
            else:
                safe_reports.append(0)

    print(f"Solution part2: {sum(safe_reports)}")


def report_is_safe(levels):
    levels_asc = sorted(levels)
    levels_desc = sorted(levels, reverse=True)
    # Check levels order
    if levels != levels_asc and levels != levels_desc:
        # print(levels, "order", levels_asc, levels_desc)
        return False
    # Check increase/decrease restrictions
    for index, value in enumerate(levels):
        if len(levels) == index + 1:
            break  # We have reached end
        diff = abs(value - levels[index + 1])
        if diff == 0 or diff > 3:
            return False
    return True  # In any other case


def main():
    with open("input.txt", "r") as file:
        # Converts file into list
        # strips newline
        # splits each line by whitespace into an array
        # casts each value of the array to integer
        # in lists we have a list of arrays of lists of two integers each
        reports = [list(map(int, line.strip().split())) for line in file]

    part1(reports)
    part2(reports)


if __name__ == "__main__":
    main()
