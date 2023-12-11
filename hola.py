def classify_hand(hand):
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

# Example usage:
hand1 = 'AAAAA'
hand2 = 'KKKKK'
hand3 = 'AA8AA'
hand4 = '23332'
hand5 = 'TTT98'
hand6 = '23432'
hand7 = 'A23A4'
hand8 = '23456'

print(classify_hand(hand1))  # Output: Five of a kind
print(classify_hand(hand2))  # Output: Five of a kind
print(classify_hand(hand3))  # Output: Four of a kind
print(classify_hand(hand4))  # Output: Full house
print(classify_hand(hand5))  # Output: Three of a kind
print(classify_hand(hand6))  # Output: Two pair
print(classify_hand(hand7))  # Output: One pair
print(classify_hand(hand8))  # Output: High card
