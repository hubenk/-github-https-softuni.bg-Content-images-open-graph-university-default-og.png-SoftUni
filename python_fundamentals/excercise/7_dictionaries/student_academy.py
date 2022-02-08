pairs = int(input())
student_diary = {}

for _ in range(pairs):
    student = input()
    grade = float(input())

    if student not in student_diary:
        student_diary[student] = grade
    else:
        student_diary[student] += grade
        student_diary[student] /= 2

for key, value in student_diary.items():
    if value >= 4.50:
        print(f"{key} -> {value:.2f}")
