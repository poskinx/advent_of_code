import string

with open("./input_1.txt") as f:
    lines = f.read()

_input = lines.split("\n")  # this way we have a last empty item in list

items = list(string.ascii_lowercase) + list(string.ascii_uppercase)
items_dict = {}
sum_of_priorities = 0
for idx, item in enumerate(items, 1):
    items_dict[item] = idx
for index in range(0, len(_input) - 1, 3):
    first_backpack = set(_input[index])
    second_backpack = set(_input[index + 1])
    third_backpack = set(_input[index + 2])
    for item in first_backpack:
        if item in second_backpack and item in third_backpack:
            sum_of_priorities += items_dict[item]
print(sum_of_priorities)
