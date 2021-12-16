jury = int(input())
presentation_assessment = 0
final_assessment = 0
students_final_assessment = 0
presentations = 0

while True:
    presentation = input()

    if presentation == "Finish":
        average_assessment = students_final_assessment / presentations
        print(f"Student's final assessment is {average_assessment:.2f}.")
        break

    for x in range(jury):

        assessment = float(input())
        presentation_assessment += assessment

    final_assessment = presentation_assessment / jury
    students_final_assessment += final_assessment
    presentations += 1
    presentation_assessment = 0

    print(f"{presentation} - {final_assessment:.2f}.")

    final_assessment = 0
