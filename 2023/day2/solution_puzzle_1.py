from collections import defaultdict


def round_is_true(round_filter, game):
    conditions = [
        round_filter['red'] >= game['red'],
        round_filter['green'] >= game['green'],
        round_filter['blue'] >= game['blue'],
    ]
    return all(conditions)


def main():
    games_count = defaultdict()
    round_filter = {'red': 12, 'green': 13, 'blue': 14}
    game_ids = []
    with open("input.txt", "r") as file:
        for line in file:
            game_is_true = True
            game, subsets = line.strip().split(':')
            games_count[game] = defaultdict(int)
            for subset in subsets.lstrip().split(';'):
                colors_count = {'red': 0, 'blue': 0, 'green': 0}
                for cubes in subset.split(','):
                    count, color = cubes.lstrip().split(' ')
                    games_count[game][color] += int(count)
                    colors_count[color] = int(count)
                if not round_is_true(round_filter, colors_count):
                    game_is_true = False
            if game_is_true:
                game_ids.append(int(game.split(' ')[1]))
    print(games_count)
    print(f"First puzzle solution {sum(game_ids)}")

if __name__ == "__main__":
    main()

