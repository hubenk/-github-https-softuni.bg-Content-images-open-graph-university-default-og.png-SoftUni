command = input()
students = {}
submissions = {}

while command != "exam finished":
    participation = command.split("-")

    if participation[1] == "banned":
        del students[participation[0]]
    else:
        name, language, points = participation

        if name not in students:
            students[name] = [points]
            if language not in submissions:
                submissions[language] = 1
            else:
                submissions[language] += 1
        else:
            if points > students[name][0]:
                students[name] = points
            submissions[language] += 1

    command = input()

print("Results:")
for key, value in students.items():
    print(f"{key} | {''.join(value)}")

print("Submissions:")
for key, value in submissions.items():
    print(f"{key} - {value}")
