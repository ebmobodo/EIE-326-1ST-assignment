# GPA Calculator using 5-point scale
# A = 5, B = 4, C = 3, D = 2, F = 0

def main():
    # Mapping of grades to points
    grade_map = {
        'A': 5.0,
        'B': 4.0,
        'C': 3.0,
        'D': 2.0,
        'F': 0.0
    }

    total_points = 0.0
    total_credits = 0.0

    print("GPA Calculator (5-Point Scale)")
    print("Enter your grades and credit unit for 6 courses:\n")

    
    for i in range(1, 7):
        print("Course", i)
        grade = input("  Enter grade (A, B, C, D, F): ").upper()

        if grade in grade_map:
            grade_point = grade_map[grade]
        else:
            print("  Invalid grade entered. Assuming F (0 points).")
            grade_point = 0.0

        credit = int(input("  Enter credit unit: "))

        total_points += grade_point * credit
        total_credits += credit

    # Calculate GPA
    if total_credits == 0:
        print("\nCannot calculate GPA. Total credit hours is zero.")
    else:
        gpa = total_points / total_credits
        print("\nYour GPA is:", round(gpa, 2))


# Run the program
if __name__ == "__main__":
    main()