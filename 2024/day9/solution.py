def part1(lines):
    # 1. convert to block format, first file, then free space, then file, etc
    #    probably good idea to store left most value block and last block
    disk_map = lines[0]
    block_ID = 0
    file_flag = True
    block_format = []
    first_no_block_position = None
    last_block_position = None
    for digit in disk_map:
        if file_flag:
            block_format.extend(str(block_ID) * int(digit))
            block_ID += 1
            if first_no_block_position is None:
                first_no_block_position = len(block_format)
            last_block_position = len(block_format) - 1
            file_flag = False
        else:
            block_format.extend("." * int(digit))
            file_flag = True
    print("block_format:", "".join(block_format))
    # 2. move around to left most
    while first_no_block_position <= last_block_position:
        next_block = block_format[last_block_position]
        while next_block == ".":
            last_block_position -= 1
            next_block = block_format[last_block_position]

        next_freespace = block_format[first_no_block_position]
        while next_freespace != ".":
            first_no_block_position += 1
            next_freespace = block_format[first_no_block_position]

        block_format.pop(first_no_block_position)
        block_format.append(".")
        block_format.insert(first_no_block_position, next_block)
        block_format.pop(last_block_position)
        first_no_block_position += 1
        last_block_position -= 1
    print("moved blocks", "".join(block_format))

    # 3. multiply by indexes and sum
    count = 0
    for i, block in enumerate(block_format):
        if block == ".":
            break
        count += i * int(block)
    print(f"Solution part1: {count}")


def part2(lines):
    # 1. convert to block format, first file, then free space, then file, etc
    #    probably good idea to store left most value block and last block
    disk_map = lines[0]
    block_ID = 0
    file_flag = True
    block_format = []
    first_no_block_position = None
    last_block_position = None
    for digit in disk_map:
        if file_flag:
            block_format.append(str(block_ID) * int(digit))
            block_ID += 1
            if first_no_block_position is None:
                first_no_block_position = len(block_format)
            last_block_position = len(block_format) - 1
            file_flag = False
        else:
            if digit != "0":
                block_format.append("." * int(digit))
            file_flag = True
    print("block_format:", block_format)
    print("first no block:", first_no_block_position)
    print("last block:", last_block_position)
    # 2. move around to left most
    while first_no_block_position <= last_block_position:
        next_block = block_format[last_block_position]
        while "." in next_block:
            last_block_position -= 1
            next_block = block_format[last_block_position]

        next_freespace = block_format[first_no_block_position]
        while "." not in next_freespace:
            first_no_block_position += 1
            next_freespace = block_format[first_no_block_position]

        block_format.pop(first_no_block_position)
        block_format.append(".")
        block_format.insert(first_no_block_position, next_block)
        block_format.pop(last_block_position)
        first_no_block_position += 1
        last_block_position -= 1
    print("moved blocks", "".join(block_format))

    # 3. multiply by indexes and sum
    count = 0
    for i, block in enumerate(block_format):
        if block == ".":
            break
        count += i * int(block)
    print(f"Solution part2: {count}")


def main():
    with open("input.txt.test", "r") as file:
        # Converts file into list
        # strips newline for each line
        lines = [line.strip() for line in file]

    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
