from collections import defaultdict


results = []


def add_cards_recursive(card_ref, cards):
    # all_cards = defaultdict(list)
    #     all_cards[card].append(card)
    #     all_cards[card].extend(copies)
    for card in cards:
        results.append(card)
        copies = card_ref[card]
        if copies:
            add_cards_recursive(card_ref, copies)


def get_matches(info):
    winning_info, my_info = info.split(" | ")
    # print(f"Winning info, my info: {winning_info, my_info}")
    winning_nums = winning_info.replace("  ", " ").split(" ")
    # print(f"Winning nums: {winning_nums}")
    my_nums = my_info.replace("  ", " ").split(" ")
    # print(f"My nums: {my_nums}")
    matches = 0
    for num in winning_nums:
        if num in my_nums:
            matches += 1
    # print(f"Matches: {matches}")
    return matches


def main():
    card_ref = defaultdict(list)
    # with open("test_input_puzzle_1.txt", "r") as file:
    with open("input.txt", "r") as file:
        for line in file:
            card, info = line.strip().split(": ")
            card_name, card_num = card.replace("   ", " ").replace("  ", " ").split(" ")
            # print(f"Card, info: {card, info}")
            matches = get_matches(info)
            # print(card, matches)
            if matches == 0:
                card_ref[card] = []
            for x in range(int(card_num) + 1, int(card_num) + matches + 1):
                # print(card)
                card_ref[card_name + " " + card_num].append(" ".join(["Card", str(x)]))
    print(card_ref)
    cards = list(card_ref.keys())
    print(cards)
    add_cards_recursive(card_ref, cards)
    # print(f"First puzzle solution {results}")
    print(f"First puzzle solution {len(results)}")


if __name__ == "__main__":
    main()
