def show_menu():
    """Display the menu options."""
    print("================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def calculate_average(scores):
    """Return the average of a list of scores, rounded to 2 decimal places."""
    total = 0
    for score in scores:
        total += score
    return round(total / len(scores), 2)


def add_student(students):
    """Prompt for name, ID, and scores, then save the student record."""
    name = input("Student name: ")
    student_id = int(input("Student ID: "))
    num_scores = int(input("How many scores? "))

    scores = []
    for i in range(num_scores):
        score = int(input(f"Enter score {i + 1}: "))
        scores.append(score)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)
    print(f'Student "{name}" added successfully.')


def display_all_students(students):
    """Print a formatted table of every student's name, ID, scores, and average."""
    if not students:
        print("No students have been added yet.")
        return

    print("-" * 50)
    print(f"{'Name':<15}{'ID':<12}{'Scores':<15}{'Average':<10}")
    print("-" * 50)

    for student in students:
        scores_str = ", ".join(str(s) for s in student["scores"])
        average = calculate_average(student["scores"])
        print(f"{student['name']:<15}{student['id']:<12}{scores_str:<15}{average:<10}")

    print("-" * 50)


def find_student_average(students):
    """Ask for a student ID, find the student, and display their average score."""
    student_id = int(input("Enter student ID: "))

    for student in students:
        if student["id"] == student_id:
            average = calculate_average(student["scores"])
            print(f"{student['name']}'s average score: {average}")
            return

    print("Error: No student found with that ID.")


def main():
    students = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        print()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            find_student_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number from 1 to 4.")

        print()


if __name__ == "__main__":
    main()