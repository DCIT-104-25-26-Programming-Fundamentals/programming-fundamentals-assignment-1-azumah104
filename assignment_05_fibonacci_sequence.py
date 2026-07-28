def generate_fibonacci(n):
    """Return a list of the first n Fibonacci numbers, using a loop."""
    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


def print_first_n_terms():
    """Part A: Ask for N and print the first N Fibonacci terms."""
    n = int(input("How many terms? "))

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    sequence = generate_fibonacci(n)
    print("Fibonacci sequence:", " ".join(str(num) for num in sequence))


def is_fibonacci_number(num):
    """Return True if num appears in the Fibonacci sequence, using a loop."""
    if num < 0:
        return False

    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b

    return False


def check_number():
    """Part B: Ask for a number and check if it's a Fibonacci number."""
    num = int(input("Enter a number to check: "))

    if is_fibonacci_number(num):
        print(f"{num} is a Fibonacci number.")
    else:
        print(f"{num} is NOT a Fibonacci number.")


def main():
    print_first_n_terms()
    print()
    check_number()


if __name__ == "__main__":
    main()