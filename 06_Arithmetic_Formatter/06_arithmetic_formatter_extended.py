# -----------------------------------------------
# + Author: George Ezzat
# -----------------------------------------------


def validate_problem(parts):
    if len(parts) != 3:
        return "Error: Not enough operands for a problem"

    if parts[1] not in ["+", "-", "*", "/", "%", "&", "|", "^"]:
        return "Error: Operator must be in ['+', '-', '*', '/', '%', '&', '|', '^']."

    if not (parts[0].isdigit() and parts[2].isdigit()):
        return "Error: Numbers must only contain digits."

    return None


# -----------------------------------------------


def calculate_result(operand1, operator, operand2):
    num1, num2 = int(operand1), int(operand2)
    if operator == '+':
        return str(num1 + num2)
    elif operator == '-':
        return str(num1 - num2)
    elif operator == '*':
        return str(num1 * num2)
    elif operator == '/':
        return str(num1 / num2) if num2 != 0 else "±inf"
    elif operator == '%':
        return str(num1 % num2)
    elif operator == '&':
        return str(num1 & num2)
    elif operator == '|':
        return str(num1 | num2)
    elif operator == '^':
        return str(num1 ^ num2)
    return None
# -----------------------------------------------


def arithmetic_arranger(problems):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line, second_line, third_line, answers = [], [], [], []

    for problem in problems:
        parts = problem.split()

        error = validate_problem(parts)
        if error:
            return error

        operand1, operator, operand2 = parts
        result = calculate_result(operand1, operator, operand2)
        length = max(len(operand1), len(operand2), len(result)) + 2

        first_line.append(operand1.rjust(length))
        second_line.append(operator + operand2.rjust(length - 1))
        third_line.append('-' * length)
        answers.append(result.rjust(length))

    lines = [
        '  |  '.join(first_line),
        '  |  '.join(second_line),
        '  |  '.join(third_line),
        '  |  '.join(answers)
    ]

    return '\n'.join(lines)


# -----------------------------------------------


# Comprehensive Test Cases
def run_tests():
    print("=== Test 1: Basic Operations ===")
    print(arithmetic_arranger(["3801 - 2", "999 + 9999"]))
    print("\n" + "="*50 + "\n")

    print("=== Test 2: Too Many Problems ===")
    print(arithmetic_arranger(
        ["1 + 2", "3 + 4", "5 + 6", "7 + 8", "9 + 10", "11 + 12"]))
    print("\n" + "="*50 + "\n")

    print("=== Test 3: Invalid Operator ===")
    print(arithmetic_arranger(["1 $ 2"]))
    print("\n" + "="*50 + "\n")

    print("=== Test 4: Non-digit Characters ===")
    print(arithmetic_arranger(["98 + 3g5"]))
    print("\n" + "="*50 + "\n")

    print("=== Test 5: Division by Zero ===")
    print(arithmetic_arranger(["5 / 0"]))
    print("\n" + "="*50 + "\n")

    print("=== Test 6: All Operators ===")
    print(arithmetic_arranger([
        "15 + 7",
        "20 - 8",
        "6 * 9",
        "20 / 5",
        "17 % 4"
    ]))
    print("\n" + "="*50 + "\n")

    print("=== Test 7: Bitwise Operations ===")
    print(arithmetic_arranger([
        "5 & 3",
        "5 | 3",
        "5 ^ 3"
    ]))
    print("\n" + "="*50 + "\n")

    print("=== Test 8: Mixed Operations ===")
    print(arithmetic_arranger([
        "123 + 49",
        "1000 - 999",
        "12 * 12"
    ]))
    print("\n" + "="*50 + "\n")

    print("=== Test 9: Without Answers ===")
    print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43"]))
    print("\n" + "="*50 + "\n")

    print("=== Test 10: Edge Cases ===")
    print(arithmetic_arranger(["0 + 0", "9999 * 1"]))
    print("\n" + "="*50 + "\n")


# -----------------------------------------------


# Run the tests
run_tests()
