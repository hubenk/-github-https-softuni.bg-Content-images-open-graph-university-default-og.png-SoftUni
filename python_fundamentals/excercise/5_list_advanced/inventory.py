inventory = input().split(", ")
command = input().split(" - ")


while command[0] != "Craft!":

    if command[0] == "Collect":
        if command[1] not in inventory:
            inventory.append(command[1])

    elif command[0] == "Drop":
        if command[1] in inventory:
            inventory.remove(command[1])

    elif command[0] == "Combine Items":
        combination = command[1].split(":")
        if combination[0] in inventory:
            new_index = inventory.index(combination[0]) + 1
            inventory.insert(new_index, combination[1])

    elif command[0] == "Renew":
        if command[1] in inventory:
            index = inventory.index(command[1])
            renew = inventory.pop(index)
            inventory.append(renew)

    command = input().split(" - ")

print(", ".join(inventory))
