"""
Simple Command-Line Calculator
Supports: +, -, *, /, ** (power), % (modulo)
"""


def calculate(a: float, op: str, b: float) -> float:
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    elif op == "**":
        return a ** b
    elif op == "%":
        if b == 0:
            raise ZeroDivisionError("Cannot modulo by zero")
        return a % b
    else:
        raise ValueError(f"Unknown operator: {op}")


def main():
    print("=== Simple Calculator ===")
    print("Operators: + - * / ** %")
    print("Type 'q' at any prompt to quit.\n")

    while True:
        a_input = input("Enter first number: ").strip()
        if a_input.lower() == "q":
            break

        op = input("Enter operator (+ - * / ** %): ").strip()
        if op.lower() == "q":
            break

        b_input = input("Enter second number: ").strip()
        if b_input.lower() == "q":
            break

        try:
            a = float(a_input)
            b = float(b_input)
            result = calculate(a, op, b)
            print(f"Result: {a} {op} {b} = {result}\n")
        except ValueError as e:
            print(f"Error: {e}\n")
        except ZeroDivisionError as e:
            print(f"Error: {e}\n")

    print("Goodbye!")


if __name__ == "__main__":
    main()