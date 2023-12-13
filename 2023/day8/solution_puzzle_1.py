navigation_map = {"L": 0, "R": 1}


def get_network(input_data):
    network = {}
    for raw_node in input_data:
        node, elements = raw_node.split(" = ")
        elements_list = elements.strip("()").split(", ")
        network[node] = elements_list
    return network


def main():
    with open("input.txt", "r") as file:
        # with open("test_input_puzzle_2.txt", "r") as file:
        lines = [line.strip() for line in file]

    instructions = lines[0]
    network = get_network(lines[2:])
    steps = 0
    node = "AAA"  # init node
    while node != "ZZZ":
        for instruction in instructions:
            steps += 1
            vertex = navigation_map[instruction]
            node = network[node][vertex]
            # `for` loop will break when while condition is true

    print(f"Puzzle solution {steps}")


if __name__ == "__main__":
    main()
