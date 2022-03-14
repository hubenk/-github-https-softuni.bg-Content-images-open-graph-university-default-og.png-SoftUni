from math import ceil

students = int(input())
lectures = int(input())
bonus = int(input())

max_bonus = 0
best_attendances = 0

for student in range(students):
    attendances = int(input())

    total_bonus = attendances / lectures * (5 + bonus)

    if total_bonus > max_bonus:
        max_bonus = total_bonus
        best_attendances = attendances

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {ceil(best_attendances)} lectures.")
