
# University Scholarship Allocation System

students = []

n = int(input("Enter number of students: "))

# Eligibility criteria
MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 40
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = list(map(int, input("Enter marks in 5 subjects: ").split()))
    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    aggregate = sum(marks) / len(marks)

    # Check eligibility
    if (aggregate >= MIN_AGGREGATE
            and min(marks) >= MIN_SUBJECT_MARKS
            and attendance >= MIN_ATTENDANCE
            and income <= MAX_INCOME):

        students.append({
            "name": name,
            "roll_no": roll_no,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

# Ranking and tie-breaking rules:
# 1. Higher aggregate marks
# 2. Higher attendance
# 3. Lower family income
# 4. Roll number in ascending order

students.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        s["roll_no"]
    )
)

# Display results
print("\n========== SCHOLARSHIP RESULTS ==========")

if len(students) == 0:
    print("No eligible students found.")
else:
    print("\nRank  Name          Roll No   Aggregate  Attendance  Income")

    for rank, s in enumerate(students, start=1):
        print(
            f"{rank:<6}"
            f"{s['name']:<14}"
            f"{s['roll_no']:<10}"
            f"{s['aggregate']:<11.2f}"
            f"{s['attendance']:<12.2f}"
            f"Rs.{s['income']:.2f}"
        )

    print("\nTotal eligible students:", len(students))
    print("Scholarship allocation ranking completed.")
