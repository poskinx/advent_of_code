from collections import defaultdict

import numpy as np


def calculate_game_power(game):
    return np.prod(list(game.values()))


def main():
    games = defaultdict()
    games_powers = []
    with open("input.txt", "r") as file:
        for line in file:
            game, subsets = line.strip().split(":")
            colors_cubes = {"red": 0, "blue": 0, "green": 0}
            games[game] = colors_cubes
            for subset in subsets.lstrip().split(";"):
                for cubes in subset.split(","):
                    cubes, color = cubes.lstrip().split(" ")
                    games[game][color] = max(games[game][color], int(cubes))
            games_powers.append(np.prod(list(games[game].values())))
    print(games)
    print(f"First puzzle solution {sum(games_powers)}")


if __name__ == "__main__":
    main()
