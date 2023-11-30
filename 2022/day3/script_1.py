import string

with open("./input_1.txt") as f:
    lines = f.read()

_input = lines.split("\n")  # this way we have a last empty item in list

items = list(string.ascii_lowercase) + list(string.ascii_uppercase)
items_dict = {}
sum_of_priorities = 0
for idx, item in enumerate(items, 1):
    items_dict[item] = idx
for backpack in _input:
    half_len = len(backpack) / 2
    first_half = set(backpack[: int(half_len)])
    second_half = set(backpack[int(half_len) :])
    for item in first_half:
        if item in second_half:
            sum_of_priorities += items_dict[item]

print(sum_of_priorities)
