initial_treasure = input().split("|")
command = input().split()
treasure_gained = 0
stolen_items = []

while command[0] != "Yohoho!":

    if command[0] == "Loot":
        for x in range(1, len(command)):
            if command[x] not in initial_treasure:
                initial_treasure.insert(0, command[x])

    elif command[0] == "Drop":
        index = int(command[1])
        if index < len(initial_treasure):
            drop_item = initial_treasure.pop(index)
            initial_treasure.append(drop_item)

    elif command[0] == "Steal":
        steal = int(command[1])
        if steal > len(initial_treasure):
            steal = len(initial_treasure)

        stolen = len(initial_treasure) - steal
        stolen_items = [item for item in initial_treasure[stolen:]]
        initial_treasure = [item for item in initial_treasure if item not in stolen_items]
        print(", ".join(stolen_items))

    command = input().split()

if len(initial_treasure) > 0:
    for item in initial_treasure:
        treasure_gained += len(item)
    avg_treasure_gain = treasure_gained / len(initial_treasure)
    print(f"Average treasure gain: {avg_treasure_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")

