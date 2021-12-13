students = int(input())
top = 0
between45 = 0
between34 = 0
under3 = 0
grade = 0

for x in range(1, students + 1):
    mark = float(input())

    if mark < 3:
        under3 += 1
        grade += mark
    elif mark <= 3.99:
        between34 += 1
        grade += mark
    elif mark <= 4.99:
        between45 += 1
        grade += mark
    elif mark <= 6:
        top += 1
        grade += mark

avg_grade = grade / students
top_percent = top / students * 100
between45_percent = between45 / students * 100
between34_percent = between34 / students * 100
under3_percent = under3 / students * 100

print(f"Top students: {top_percent:.2f}%")
print(f"Between 4.00 and 4.99: {between45_percent:.2f}%")
print(f"Between 3.00 and 3.99: {between34_percent:.2f}%")
print(f"Fail: {under3_percent:.2f}%")
print(f"Average: {avg_grade:.2f}")