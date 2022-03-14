initial_list = input().split("!")

command = input()
while command != "Go Shopping!":
    actions = command.split()

    if actions[0] == "Urgent":
        if actions[1] not in initial_list:
            initial_list.insert(0, actions[1])

    elif actions[0] == "Unnecessary":
        if actions[1] in initial_list:
            initial_list.remove(actions[1])

    elif actions[0] == "Correct":
        if actions[1] in initial_list:
            index = initial_list.index(actions[1])
            initial_list[index] = actions[2]

    elif actions[0] == "Rearrange":
        if actions[1] in initial_list:
            initial_list.remove(actions[1])
            initial_list.append(actions[1])

    command = input()

print(", ".join(initial_list))