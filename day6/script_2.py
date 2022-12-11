if __name__ == "__main__":
    with open("./input_1.txt") as f:
        lines = f.read()

    _input = lines.split("\n")
    data = _input[0]
    for index in range(1, len(data), 1):
        last_four_chars = data[index-1:index+13]
        if len(set(x for x in last_four_chars)) == 14:
            print(index+13)
            break
        
