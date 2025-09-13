def validate_problem(parts):
    if len(parts) != 3:
        return "Error: Not enough operands for a problem"

    if parts[1] not in ["+", "-"]:
        return "Error: Operator must be '+' or '-'."

    if not (parts[0].isdigit() and parts[2].isdigit()):
        return "Error: Numbers must only contain digits."

    if len(parts[0]) > 4 or len(parts[2]) > 4:
        return "Error: Numbers cannot be more than four digits."

    return None


# -----------------------------------------------


def calculate_result(operand1, operator, operand2):
    num1, num2 = int(operand1), int(operand2)
    return str(num1 + num2) if operator == '+' else str(num1 - num2)


# -----------------------------------------------


def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line, second_line, third_line, answers = [], [], [], []

    for problem in problems:
        parts = problem.split()

        error = validate_problem(parts)
        if error:
            return error

        operand1, operator, operand2 = parts
        length = max(len(operand1), len(operand2)) + 2

        first_line.append(operand1.rjust(length))
        second_line.append(operator + operand2.rjust(length - 1))
        third_line.append('-' * length)

        if show_answers:
            result = calculate_result(operand1, operator, operand2)
            answers.append(result.rjust(length))

    lines = [
        '  |  '.join(first_line),
        '  |  '.join(second_line),
        '  |  '.join(third_line),
    ]

    if show_answers:
        lines.append('  |  '.join(answers))

    return '\n'.join(lines)


# -----------------------------------------------


# Comprehensive Test Cases
def run_tests():
    print("=== Test 1: Basic Operations with Answers ===")
    print(arithmetic_arranger(["3801 - 2", "123 + 49"], show_answers=True))
    print("\n" + "="*50 + "\n")

    print("=== Test 2: Basic Operations without Answers ===")
    print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"]))
    print("\n" + "="*50 + "\n")

    print("=== Test 3: Too Many Problems ===")
    print(arithmetic_arranger(
        ["1 + 2", "3 - 4", "5 + 6", "7 - 8", "9 + 10", "11 - 12"]))
    print("\n" + "="*50 + "\n")

    print("=== Test 4: Invalid Operator ===")
    print(arithmetic_arranger(["1 * 2", "4 / 2"]))
    print("\n" + "="*50 + "\n")

    print("=== Test 5: Non-digit Characters ===")
    print(arithmetic_arranger(["98 + 3g5", "22 - 1a"]))
    print("\n" + "="*50 + "\n")

    print("=== Test 6: Number Too Long ===")
    print(arithmetic_arranger(["9999 + 1", "12345 - 5"]))
    print("\n" + "="*50 + "\n")


# -----------------------------------------------


# Run the tests
run_tests()
