
# Examination Result and Grace-Mark Validation

subjects = []
n = int(input("Enter number of subjects: "))

if n <= 0:
    print("Invalid number of subjects.")

else:
    total_marks = 0
    total_maximum = 0
    grace_used = 0
    failed_subjects = 0

    for i in range(n):
        print("\nSubject", i + 1)

        name = input("Enter subject name: ")
        maximum = int(input("Enter maximum marks: "))
        pass_mark = int(input("Enter minimum pass marks: "))
        marks = int(input("Enter obtained marks: "))

        # Validate marks
        if (maximum <= 0 or pass_mark < 0
                or pass_mark > maximum
                or marks < 0 or marks > maximum):
            print("Invalid marks or pass criteria.")
            subjects = []
            break

        # Grace policy: maximum 5 marks per subject,
        # only if the student is short by at most 5 marks.
        grace = 0

        if marks < pass_mark:
            shortage = pass_mark - marks

            if shortage <= 5:
                grace = shortage
                marks = min(marks + grace, maximum)

        final_marks = marks
        passed = final_marks >= pass_mark

        if not passed:
            failed_subjects += 1

        grace_used += grace
        total_marks += final_marks
        total_maximum += maximum

        subjects.append({
            "name": name,
            "marks": final_marks,
            "maximum": maximum,
            "grace": grace,
            "passed": passed
        })

    if len(subjects) == n:
        percentage = total_marks / total_maximum * 100

        print("\n========== FINAL EXAMINATION RESULT ==========")

        print("\nSubject       Marks   Grace   Result")

        for s in subjects:
            status = "PASS" if s["passed"] else "FAIL"
            print(
                f"{s['name']:<14}"
                f"{s['marks']:<8}"
                f"{s['grace']:<8}"
                f"{status}"
            )

        print("\nTotal Marks:", total_marks, "/", total_maximum)
        print("Percentage:", round(percentage, 2), "%")
        print("Total Grace Marks:", grace_used)

        if failed_subjects > 0:
            classification = "FAIL"
        elif percentage >= 75:
            classification = "DISTINCTION"
        elif percentage >= 60:
            classification = "FIRST CLASS"
        elif percentage >= 50:
            classification = "SECOND CLASS"
        else:
            classification = "PASS"

        print("Final Classification:", classification)
