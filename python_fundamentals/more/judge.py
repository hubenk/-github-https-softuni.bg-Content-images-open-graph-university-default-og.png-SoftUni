data = input()
contest_participants = {}
individual_standings = {}

while data != "no more time":
    username, contest, points = data.split(" -> ")

    if contest not in contest_participants:
        contest_participants[contest] = {}

    if username not in contest_participants[contest]:
        contest_participants[contest][username] = int(points)
    elif contest_participants[contest][username] < int(points):
        contest_participants[contest][username] = int(points)

    data = input()

for course in contest_participants.keys():
    for name, points in contest_participants[course].items():
        if name not in individual_standings:
            individual_standings[name] = int(points)
        else:
            individual_standings[name] += int(points)

for contest, user in contest_participants.items():
    print(f"{contest}: {len(contest_participants[contest])} participants")
    counter = 1
    for username, points in sorted(contest_participants[contest].items(), reverse=False, key=lambda x: (-x[1], x[0])):
        print(f"{counter}. {username} <::> {points}")
        counter += 1
print("Individual standings:")
counter = 1
for user, points in sorted(individual_standings.items(), reverse=False, key=lambda x: (-x[1], x[0])):
    print(f"{counter}. {user} -> {points}")
    counter += 1