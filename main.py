"""Simple command-line calculator (SWYNEX Task 1 sample app)."""

from src.calculator import add, subtract, multiply, divide

OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def main() -> None:
    print("SWYNEX Calculator (type 'q' to quit)")
    while True:
        first = input("Enter first number: ").strip()
        if first.lower() == "q":
            break
        op = input("Enter operation (+, -, *, /): ").strip()
        second = input("Enter second number: ").strip()

        if op not in OPERATIONS:
            print("Invalid operation. Use +, -, * or /.")
            continue
        try:
            result = OPERATIONS[op](float(first), float(second))
            print(f"Result: {result}")
        except ValueError as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    main()
