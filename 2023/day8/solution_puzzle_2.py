import numpy as np


navigation_map = {"L": 0, "R": 1}


def get_init_nodes_network(input_data):
    network = {}
    init_nodes = []
    for raw_node in input_data:
        node, elements = raw_node.split(" = ")
        elements_list = elements.strip("()").split(", ")
        network[node] = elements_list
        if node.endswith("A"):
            init_nodes.append(node)
    return init_nodes, network


def main():
    with open("input.txt", "r") as file:
        # with open("test_input_puzzle_3.txt", "r") as file:
        lines = [line.strip() for line in file]

    instructions = lines[0]
    init_nodes, network = get_init_nodes_network(lines[2:])
    steps_list = []
    for node in init_nodes:
        steps = 0
        while not node.endswith("Z"):
            for instruction in instructions:
                steps += 1
                vertex = navigation_map[instruction]
                node = network[node][vertex]
        steps_list.append(steps)

    print(f"Puzzle solution {np.lcm.reduce(steps_list)}")


if __name__ == "__main__":
    main()
