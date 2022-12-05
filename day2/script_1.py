with open("./input_1.txt") as f:
    lines = f.read()

_input = lines.split("\n")  # this way we have a last empty item in list

A = X = 1  # rock
B = Y = 2  # paper
C = Z = 3  # scissors
opponent_play = {"A": "X", "B": "Y", "C": "Z"}
my_dict = {"X": X, "Y": Y, "Z": Z}

loss = 0
draw = 3
win = 6

victories = {
    "X": "C",
    "Y": "A",
    "Z": "B",
}
total_score = 0
for _round in _input:
    if not _round:
        break
    opponent, me = _round.split(" ")
    defeats = victories[me]  # C
    if opponent_play[opponent] == me:
        total_score += my_dict[me] + draw
        print("draw", defeats, opponent, me, my_dict[me], draw)
    elif opponent == defeats:
        total_score += my_dict[me] + win
        print("win", defeats, opponent, me, my_dict[me], win)
    else:
        total_score += my_dict[me] + loss
        print("loss", defeats, opponent, me, my_dict[me], loss)

print(total_score)
