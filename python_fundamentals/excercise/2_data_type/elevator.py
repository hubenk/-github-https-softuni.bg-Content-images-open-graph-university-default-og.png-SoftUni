persons = int(input())
capacy = int(input())

full_courses = persons // capacy

if persons % capacy != 0:
    full_courses += 1

print(full_courses)
