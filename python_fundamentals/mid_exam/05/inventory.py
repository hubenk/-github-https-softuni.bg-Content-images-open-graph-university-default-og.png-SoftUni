journal = input().split(", ")

commands = input()

while commands != "Craft!":
    command, item = commands.split(" - ")

    if command == "Collect":
        if item not in journal:
            journal.append(item)

    elif command == "Drop":
        if item in journal:
            journal.remove(item)

    elif command == "Combine Items":
        item1, item2 = item.split(":")
        if item1 in journal:
            item_index = journal.index(item1)
            journal.insert(item_index + 1, item2)

    elif command == "Renew":
        if item in journal:
            item_index = journal.index(item)
            journal.pop(item_index)
            journal.append(item)

    commands = input()

print(", ".join(journal))
