targets = [int(x) for x in input().split()]
command = input()

while command != "End":
    command = command.split()

    if command[0] == "Shoot" and int(command[1]) < len(targets):
        index = int(command[1])
        targets[index] -= int(command[2])
        if targets[index] <= 0:
            targets.pop(index)

    elif command[0] == "Add":
        index = int(command[1])
        if index >= len(targets):
            print("Invalid placement!")
        else:
            targets.insert(index, int(command[2]))

    elif command[0] == "Strike":
        index = int(command[1])
        if index + int(command[2]) >= len(targets):
            print("Strike missed!")
        else:
            targets.pop(index + 1)
            targets.pop(index)
            targets.pop(index - 1)

    command = input()

targets = [str(x) for x in targets]
print("|".join(targets))
