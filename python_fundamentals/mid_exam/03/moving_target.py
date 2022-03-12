targets = [int(x) for x in input().split()]
command = input()

while command != "End":
    action, index, other = command.split()

    if action == "Shoot" and int(index) <= len(targets):
        targets[int(index)] -= int(other)
        if targets[int(index)] <= 0:
            targets.pop(int(index))

    elif action == "Add":
        if int(index) >= len(targets):
            print("Invalid placement!")
        else:
            targets.insert(int(index), int(other))

    elif action == "Strike":
        if int(index) + int(other) > len(targets) or int(index) - int(other) < 0:
            print("Strike missed!")
        else:
            del targets[int(index) - int(other):int(index) + int(other)+1]

    command = input()

targets = [str(x) for x in targets]
print("|".join(targets))
