with open("./input_1.txt") as f:
    lines = f.read()

_input = lines.split("\n")  # this way we have a last empty item in list

A = 1  # rock
B = 2  # paper
C = 3  # scissors

loss = 0
draw = 3
win = 6

victories = {
    "A": "C",
    "B": "A",
    "C": "B",
}
defeats = {
    "C": "A",
    "A": "B",
    "B": "C",
}
values = {"A": A, "B": B, "C": C}
total_score = 0
for _round in _input:
    if not _round:
        break
    opponent, me = _round.split(" ")
    if me == "Y":  # draw
        total_score += values[opponent] + draw
    elif me == "X":  # loss
        total_score += values[victories[opponent]] + loss
    else:
        total_score += values[defeats[opponent]] + win

print(total_score)
