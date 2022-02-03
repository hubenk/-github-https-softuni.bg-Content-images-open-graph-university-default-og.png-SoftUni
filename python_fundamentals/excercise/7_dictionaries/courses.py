command = input().split(":")
courses = {}

while command[0] != "end":
    main_course = command[0][:-1]

    if main_course not in courses:
        courses[main_course] = []

    courses[main_course].append(command[1])

    command = input().split(":")

for course in courses:
    print(f"{course}: {len(courses[course])}")
    for student in courses[course]:
        print(f"--{student}")