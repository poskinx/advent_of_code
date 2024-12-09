import re


def part1(instructions):
    real_instructions = get_real_instructions(instructions)
    results = []
    for matches in real_instructions:
        for expression in matches:
            result = multiply_from_string(expression)
            results.append(result)
    print(f"Solution part1: {sum(results)}")


def part2(instructions):
    enabled_instructions = get_enabled_instructions(instructions)
    results = []
    for matches in enabled_instructions:
        for expression in matches:
            result = multiply_from_string(expression)
            results.append(result)
    print(f"Solution part2: {sum(results)}")


def multiply_from_string(expression):
    """
    Extracts the numbers from a string in the format 'mul(X,Y)'
    and returns the result of multiplying X and Y.

    Args:
        expression (str): A string in the format 'mul(X,Y)' where X and Y are 1-3 digit numbers.

    Returns:
        int: The result of multiplying X and Y.

    Raises:
        ValueError: If the input string is not in the correct format.
    """
    # Regex pattern to match "mul(X,Y)" where X and Y are 1-3 digit numbers
    pattern = r"^mul\((\d{1,3}),(\d{1,3})\)$"

    # Match the pattern
    match = re.match(pattern, expression)

    if not match:
        raise ValueError("Invalid input format. Expected 'mul(X,Y)' where X and Y are 1-3 digit numbers.")

    # Extract X and Y as integers
    x, y = map(int, match.groups())

    # Return the product
    return x * y


def get_enabled_instructions(instructions):
    """
    Extracts the `mul(X,Y)` instructions from the input string where `X` and `Y` are 1-3 digit numbers,
    based on the most recent `do()` or `don't()` instruction.

    Args:
        instructions (list): The input list containing instruction strings.

    Returns:
        list: A list of enabled `mul(X,Y)` instructions as strings.
    """

    # Find all mul and control instructions in the order they appear
    enabled_instructions = []
    # Tricky part to put enable here. The instructions should be analyzed as a  whole
    enabled = True
    for instruction in instructions:
        matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", instruction)
        # Track if mul instructions are enabled (default is enabled)
        result = []
        # Process instructions
        for match in matches:
            if match == "do()":
                enabled = True
            elif match == "don't()":
                enabled = False
            elif enabled and match.startswith("mul"):
                result.append(match)
        enabled_instructions.append(result)
    return enabled_instructions


def get_real_instructions(instructions):
    # Regex pattern to match "mul(X,Y)" where X and Y are 1-3 digit numbers
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    # Find all matches
    real_instructions = []
    for instruction in instructions:
        matches = re.findall(pattern, instruction)
        real_instructions.append(matches)
    return real_instructions


def main():
    with open("input.txt", "r") as file:
        # Converts file into list
        # strips newline
        # splits each line by whitespace into an array
        # in instructions we have a list of arrays of lists of two integers each
        instructions = [line for line in file]

    part1(instructions)
    part2(instructions)


if __name__ == "__main__":
    main()
