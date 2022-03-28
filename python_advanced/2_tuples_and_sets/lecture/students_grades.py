from statistics import mean

students_number = int(input())
students = {}

for _ in range(students_number):
    name, grade = input().split()

    if name not in students:
        students[name] = [float(grade)]
    else:
        students[name].append(float(grade))


for key, value in students.items():
    print(f"{key} -> {' '.join([f'{x:.2f}' for x in value])} (avg: {mean(value):.2f})")
    # print(f"{key} -> {' '.join([f'{x:.2f}' for x in value])} (avg: {(sum(value) / len(value)):.2f})")
