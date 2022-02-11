contest_passwords = input()
passwords_dict = {}
users_dict = {}
best_cantidate = {}

while contest_passwords != "end of contests":
    contest, password = contest_passwords.split(":")

    if contest not in passwords_dict:
        passwords_dict[contest] = password

    contest_passwords = input()

users = input()

while users != "end of submissions":
    contest, password, username, points = users.split("=>")

    if contest in passwords_dict:
        if passwords_dict[contest] == password:
            if username not in users_dict:
                users_dict[username] = {}
            if username in users_dict:
                if contest in users_dict[username]:
                    if int(points) > int(users_dict[username][contest]):
                        users_dict[username][contest] = points
                else:
                    users_dict[username][contest] = points
            if username not in best_cantidate:
                best_cantidate[username] = 0

    users = input()

for candidate in users_dict.keys():
    for points in users_dict[candidate].values():
        best_cantidate[candidate] += int(points)


print(f"Best candidate is {max(best_cantidate.keys())} with total {max(best_cantidate.values())} points.")
print("Ranking:")
for user, points in sorted(users_dict.items(), reverse=False, key=lambda x: x[0]):
    print(user)
    for course, po in sorted(users_dict[user].items(), reverse=True, key=lambda kvp: kvp[1]):
        print(f"#  {course} -> {po}")