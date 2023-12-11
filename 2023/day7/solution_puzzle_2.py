from collections import defaultdict, deque


card_value = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

hand_types = [
    "Five of a kind",
    "Four of a kind",
    "Full house",
    "Three of a kind",
    "Two pair",
    "One pair",
    "High card",
]


def transform_hand(hand):
    hands_by_type = defaultdict(list)
    card_ranks = [card for card in hand if card != "J"]
    ranks = []
    for card in set(card_ranks):
        transformed_hand = hand.replace("J", card)
        hand_values = [card_value[card] for card in transformed_hand]
        hand_type = classify_hand(transformed_hand)
        hands_by_type[hand_type].append([hand_values, transformed_hand])
    for hand_type in hand_types:
        ranks.extend(sort_list_of_hands(hands_by_type[hand_type]))
    try:
        return ranks[0][1]
    except IndexError:  # all Js
        return "AAAAA"


def classify_hand(hand):
    if "J" in hand:
        hand = transform_hand(hand)
    card_ranks = [card for card in hand]

    unique_ranks = set(card_ranks)
    counts = [card_ranks.count(rank) for rank in unique_ranks]

    for rank in unique_ranks:
        if rank * 5 in hand:
            return "Five of a kind"

    if 4 in counts and 1 in counts:
        return "Four of a kind"
    elif 3 in counts and 2 in counts:
        return "Full house"
    elif 3 in counts and 2 not in counts:
        return "Three of a kind"
    elif counts.count(2) == 2:
        return "Two pair"
    elif counts.count(2) == 1:
        return "One pair"
    else:
        return "High card"


def is_stronger(sorted_hand, hand):
    for card1, card2 in zip(sorted_hand, hand):
        if card2 > card1:
            return True
        elif card2 == card1:
            continue
        else:
            break
    return False


def sort_list_of_hands(hands):
    sorted_hands = deque()
    for hand, bid in hands:
        is_sorted = False
        index = 0
        for i, (sorted_hand, sorted_bid) in enumerate(sorted_hands):
            if is_stronger(sorted_hand, hand):
                is_sorted = True
                index = i
                break
        if not is_sorted:
            sorted_hands.append([hand, bid])
        else:
            sorted_hands.insert(index, [hand, bid])
    return sorted_hands


def main():
    ranks = []
    results = []
    hands_by_type = defaultdict(list)
    with open("input.txt", "r") as file:
        # with open("test_input_puzzle_1.txt", "r") as file:
        for line in file:
            hand, bid = line.strip().split(" ")
            hand_values = [card_value[card] for card in hand]
            hand_type = classify_hand(hand)
            hands_by_type[hand_type].append([hand_values, bid])
    # print(hands_by_type)
    for hand_type in hand_types:
        sorted_hands = sort_list_of_hands(hands_by_type[hand_type])
        # print(hand_type, sorted_hands)
        ranks.extend(sorted_hands)

    ranks_length = len(ranks)
    for i, (hand, bid) in enumerate(ranks):
        rank = ranks_length - i
        results.append(int(rank) * int(bid))

    # results.append(wins)
    print(f"Puzzle solution {sum(results)}")


if __name__ == "__main__":
    main()
