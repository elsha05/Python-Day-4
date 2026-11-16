
def calculate_grade(mark):
    if mark >= 90:
        return "A Grade"
    elif mark >= 75:
        return "B Grade"
    elif mark >= 50:
        return "C Grade"
    else:
        return "Fail"


def main():
    print("===== STUDENT GRADE CALCULATOR =====")

    try:
        name = input("Enter student name: ")

        total = 0

        for i in range(1, 6):
            mark = float(input(f"Enter subject {i} mark: "))

            if mark < 0 or mark > 100:
                print("Mark must be between 0 and 100")
                return

            total += mark

        average = total / 5

        print("\n===== RESULT =====")
        print("Student Name:", name)
        print("Total Marks:", total)
        print("Average:", average)
        print("Grade:", calculate_grade(average))

    except ValueError:
        print("Error: Please enter valid numbers.")


if __name__ == "__main__":
    main()

