def parse_crates(row):
    """
    The way we have parsed the input, we have in each row:
        1. Three empty spaces if there is no crate
        2. empty space to separate between stack columns
        3. [X] if there is a crate where X can be any capittal letter
    """
    row_parsed = []
    for index in range(0, len(row), 4):
        first = row[index]
        second = row[index + 1]
        third = row[index + 2]
        crate = (
            "".join([first, second, third])
            .replace(" ", "")
            .replace("[", "")
            .replace("]", "")
        )
        row_parsed.append(crate)
    return row_parsed


if __name__ == "__main__":
    with open("./input_1.txt") as f:
        lines = f.read()

    _input = lines.split("\n")
    stack_data, instructions = lines.split("\n\n")
    stack_data_lines = stack_data.split("\n")
    instructions_lines = instructions.split("\n")

    # stacks dict creation
    stacks = {}
    for idx in range(1, int(len(stack_data_lines[0].split(" ")) / 3 + 1)):
        stacks[idx] = []

    # parsing stacks data
    for row in stack_data_lines:
        if row.startswith(" 1"):
            break
        crates = parse_crates(row)
        for idx, x in enumerate(crates, 1):
            if x != "":
                stacks[idx].insert(0, x)
    print(stacks)
    for instruction in instructions_lines:
        if instruction == "":
            break
        instruction_splited = instruction.split(" ")
        num_of_crates = int(instruction_splited[1])
        from_stack = int(instruction_splited[3])
        to_stack = int(instruction_splited[5])
        for x in range(num_of_crates):
            crate = stacks[from_stack].pop()
            stacks[to_stack].append(crate)
    print(stacks)
    print("".join(value[-1:][0] for value in stacks.values()))
