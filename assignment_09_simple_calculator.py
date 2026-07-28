def show_menu():
    """Display the menu options."""
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    """Return a / b, or None if b is zero."""
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    """Return a % b, or None if b is zero."""
    if b == 0:
        return None
    return a % b


def exponentiate(a, b):
    return a ** b


def get_two_numbers():
    """Prompt for and return two numbers as floats."""
    a = float(input("Enter first number : "))
    b = float(input("Enter second number: "))
    return a, b


def main():
    symbols = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/",
        "5": "%",
        "6": "**"
    }

    while True:
        show_menu()
        choice = input("Select an operation (1-7): ")
        print()

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in symbols:
            print("Error: Invalid choice. Please enter a number from 1 to 7.")
            print()
            continue

        a, b = get_two_numbers()
        symbol = symbols[choice]

        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = subtract(a, b)
        elif choice == "3":
            result = multiply(a, b)
        elif choice == "4":
            result = divide(a, b)
            if result is None:
                print("Error: Cannot divide by zero.")
                print()
                continue
        elif choice == "5":
            result = modulus(a, b)
            if result is None:
                print("Error: Cannot divide by zero.")
                print()
                continue
        elif choice == "6":
            result = exponentiate(a, b)

        # Clean up whole-number floats (e.g. 13.0 -> 13) for nicer display
        if result == int(result):
            result = int(result)

        print(f"Result: {a:g} {symbol} {b:g} = {result}")
        print()


if __name__ == "__main__":
    main()