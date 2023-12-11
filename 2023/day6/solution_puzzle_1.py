import numpy as np


def calculate_distance(tmax, t):
    return (tmax - t) * t


def main():
    results = []
    with open("input.txt", "r") as file:
        # with open("test_input_puzzle_1.txt", "r") as file:
        lines = [line.strip() for line in file]
    times = " ".join(lines[0].split()).replace("Time:", "")
    distances = " ".join(lines[1].split()).replace("Distance:", "")
    times = map(int, times.split())
    distances = map(int, distances.split())
    for tmax, race_distance in zip(times, distances):
        wins = 0
        for t in range(1, tmax):
            distance = calculate_distance(tmax, t)
            if distance > race_distance:
                wins += 1
        results.append(wins)
    print(f"Puzzle solution {np.prod(results)}")


if __name__ == "__main__":
    main()
