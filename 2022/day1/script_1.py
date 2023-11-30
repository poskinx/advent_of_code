with open("./input_1.txt") as f:
    lines = f.read()

_input = lines.split("\n")  # this way we have a last empty item in list

current_calories = 0
max_calories = 0

for index in range(len(_input)):
    if _input[index] != "":
        current_calories += int(_input[index])
    else:
        if current_calories > max_calories:
            max_calories = current_calories
        current_calories = 0
print(max_calories)
