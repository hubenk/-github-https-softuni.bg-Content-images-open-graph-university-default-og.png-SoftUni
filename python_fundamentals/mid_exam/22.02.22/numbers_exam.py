numbers = [int(x) for x in input().split()]

commands = input()

while commands != "Finish":
    actions = commands.split()

    if actions[0] == "Add":
        numbers.append(int(actions[1]))

    elif actions[0] == "Remove":
        if int(actions[1]) in numbers:
            numbers.remove(int(actions[1]))

    elif actions[0] == "Replace":
        for num in numbers:
            if num == int(actions[1]):
                index = numbers.index(num)
                numbers[index] = int(actions[2])
                break

    elif actions[0] == "Collapse":
        numbers = [x for x in numbers if x >= int(actions[1])]

    commands = input()

print(*numbers)
