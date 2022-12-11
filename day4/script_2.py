import string

with open("./input_1.txt") as f:
    lines = f.read()

_input = lines.split("\n")

total_pairs_fully_overlapped = 0

for section_pair in _input:
    if not section_pair:
        break
    first_elf, second_elf = [x.split("-") for x in section_pair.split(",")]
    first_elf_sections = [x for x in range(int(first_elf[0]), int(first_elf[1]) + 1, 1)]
    second_elf_sections = [
        x for x in range(int(second_elf[0]), int(second_elf[1]) + 1, 1)
    ]
    for item in first_elf_sections:
        if item in second_elf_sections:
            total_pairs_fully_overlapped += 1
            break
print(total_pairs_fully_overlapped)
