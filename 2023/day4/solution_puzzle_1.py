import math


def main():
    results = []
    # with open("test_input_puzzle_1.txt", "r") as file:
    with open("input.txt", "r") as file:
        for line in file:
            card, info = line.strip().split(': ')
            print(f"Card, info: {card, info}")
            winning_info, my_info = info.split(' | ')
            # print(f"Winning info, my info: {winning_info, my_info}")
            winning_nums = winning_info.replace('  ', ' ').split(' ')
            # print(f"Winning nums: {winning_nums}")
            my_nums = my_info.replace('  ', ' ').split(' ')
            # print(f"My nums: {my_nums}")
            matches = 0
            for num in winning_nums:
                if num in my_nums:
                    matches += 1
            print(f"Matches: {matches}, result: {math.pow(2, matches - 1)}")
            if matches != 0:
                results.append(int(math.pow(2, matches - 1)))
    print(f"First puzzle solution {sum(results)}")


if __name__ == "__main__":
    main()

