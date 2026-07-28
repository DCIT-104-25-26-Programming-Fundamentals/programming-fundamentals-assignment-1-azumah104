def calculate_sum(numbers):
    """Return the sum of all numbers, without using sum()."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Return the average of all numbers."""
    return calculate_sum(numbers) / len(numbers)


def find_maximum(numbers):
    """Return the largest number, without using max()."""
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def find_minimum(numbers):
    """Return the smallest number, without using min()."""
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest


def main():
    n = int(input("How many numbers? "))

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    numbers = []
    for i in range(n):
        value = int(input(f"Enter number {i + 1}: "))
        numbers.append(value)

    print("\nResults:")
    print(f"Sum:     {calculate_sum(numbers)}")
    print(f"Average: {calculate_average(numbers)}")
    print(f"Maximum: {find_maximum(numbers)}")
    print(f"Minimum: {find_minimum(numbers)}")


if __name__ == "__main__":
    main()