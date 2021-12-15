student = input()
grade = 1
total_mark = 0
count = 0

while grade <= 12:
    mark = float(input())
    total_mark += mark

    if mark < 4:
        count += 1
        total_mark -= mark
        if count == 1:
            continue
        else:
            print(f"{student} has been excluded at {grade} grade")
            break

    if grade == 12:
        avg = total_mark / grade
        print(f"{student} graduated. Average grade: {avg:.2f}")
        break
    else:
        grade += 1



