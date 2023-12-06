from collections import OrderedDict
from pprint import pprint


def get_destination(seed, source_to_dest, mapping):
    for _range, operation in mapping[source_to_dest]:
        if seed in _range:
            return seed + operation
    return seed


def main():
    mapping = OrderedDict()
    seeds = []
    # with open("input.txt", "r") as file:
    with open("test_input_puzzle_1.txt", "r") as file:
        for line in file:
            line = line.strip()
            if "seeds" in line:
                seeds = [int(x) for x in line.split(": ")[1].split(" ")]
            elif line:
                if "map" in line:
                    source_to_dest = line
                    mapping[source_to_dest] = []
                else:
                    dest, source, length = [int(x) for x in line.split(" ")]
                    source_range = range(source, source + length)
                    operation = dest - source
                    mapping[source_to_dest].append([source_range, operation])
    location = 0
    # pprint(mapping)
    for seed in seeds:
        for source_to_dest in mapping.keys():
            seed = get_destination(seed, source_to_dest, mapping)
        if location == 0:
            location = seed
        else:
            location = min(location, seed)
    print(f"Puzzle solution {location}")


if __name__ == "__main__":
    main()
