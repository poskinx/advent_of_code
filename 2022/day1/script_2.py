with open("./input_1.txt") as f:
    lines = f.read()

_input = lines.split("\n")  # this way we have a last empty item in list

current_calories = 0
top_3_elf_calories = [0, 0, 0]

for index in range(len(_input)):
    if _input[index] != "":
        current_calories += int(_input[index])
    else:
        top_3_elf_calories.append(current_calories)
        min_value = min(top_3_elf_calories)
        top_3_elf_calories.remove(min_value)
        current_calories = 0
print(sum(top_3_elf_calories))
