import numpy as np
from tqdm import tqdm


def calculate_distance(tmax, t):
    return (tmax - t) * t


def main():
    results = []
    with open("input.txt", "r") as file:
        # with open("test_input_puzzle_1.txt", "r") as file:
        lines = [line.strip() for line in file]

    times = lines[0].replace("Time:", "").replace(" ", "")
    distances = lines[1].replace("Distance:", "").replace(" ", "")

    times = map(int, [times])
    distances = map(int, [distances])

    for tmax, race_distance in zip(times, distances):
        wins = 0
        for t in tqdm(range(1, tmax)):
            distance = calculate_distance(tmax, t)
            if distance > race_distance:
                wins += 1
        results.append(wins)
    print(f"Puzzle solution {np.prod(results)}")


if __name__ == "__main__":
    main()
