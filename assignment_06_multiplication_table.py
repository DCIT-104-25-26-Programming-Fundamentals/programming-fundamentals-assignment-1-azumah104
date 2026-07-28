def print_table(number):
    """Print the multiplication table for a single number, 1 to 12."""
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i:<2} = {number * i}")


def part_a_single_table():
    """Part A: Ask for a number and print its multiplication table."""
    number = int(input("Enter a number: "))
    print_table(number)


def part_b_tables_up_to_n():
    """Part B: Ask for N and print tables for every number from 1 to N."""
    n = int(input("Enter N: "))

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    for number in range(1, n + 1):
        print_table(number)
        if number != n:
            print("---------------------------")


def main():
    print("Multiplication Table Generator")
    print("1. Single Table")
    print("2. Tables from 1 to N")
    choice = input("Choose an option (1-2): ")

    if choice == "1":
        part_a_single_table()
    elif choice == "2":
        part_b_tables_up_to_n()
    else:
        print("Error: Invalid choice.")


if __name__ == "__main__":
    main()