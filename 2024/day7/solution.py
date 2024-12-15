import ast
from itertools import product


def generate_expressions(input_str, operators="*+"):
    # Split the string by whitespace to get the parts
    parts = input_str.split(" ")
    # Count the spaces (number of operators needed)
    num_spaces = len(parts) - 1
    # Generate all combinations of '*' and '+'
    operator_combinations = product(operators, repeat=num_spaces)

    # Create expressions by joining parts with operators
    expressions = []
    for ops in operator_combinations:
        # Zip parts and operators together and flatten into a string
        expression = "".join(part + op for part, op in zip(parts, ops)) + parts[-1]
        expressions.append(expression)

    return expressions


def evaluate_left_to_right(expr):
    """
    Evaluate a mathematical expression containing only +, *, and integers strictly left-to-right.
    """
    # Split the expression into tokens
    tokens = expr.replace("+", " + ").replace("*", " * ").replace("|", " | ").split()

    # Perform left-to-right evaluation
    result = int(tokens[0])  # Start with the first number
    i = 1
    while i < len(tokens):
        operator = tokens[i]
        operand = int(tokens[i + 1])
        if operator == "+":
            result += operand
        elif operator == "*":
            result *= operand
        elif operator == "|":
            result_str = str(result)
            operand_str = str(operand)
            result = int(f"{result_str}{operand_str}")
        i += 2  # Move to the next operator-operand pair

    return result


def part1(lines):
    count = 0
    for line in lines:
        test_result, equation_str = line.split(":")
        test_result = int(test_result)
        expressions = generate_expressions(equation_str.lstrip())
        for expression in expressions:
            result = evaluate_left_to_right(expression)
            if result == test_result:
                count += test_result
                break
    print(f"Solution part1: {count}")


def part2(lines):
    count = 0
    for line in lines:
        test_result, equation_str = line.split(":")
        test_result = int(test_result)
        expressions = generate_expressions(equation_str.lstrip(), operators="*+|")
        for expression in expressions:
            result = evaluate_left_to_right(expression)
            if result == test_result:
                count += test_result
                break
    print(f"Solution part2: {count}")


def main():
    with open("input.txt", "r") as file:
        # Converts file into list
        # strips newline for each line
        lines = [line.strip() for line in file]

    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
