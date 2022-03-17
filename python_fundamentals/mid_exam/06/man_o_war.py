pirate_ship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
maximum_health = int(input())

command = input()
while command != "Retire":
    action = command.split()

    if action[0] == "Fire":
        index = int(action[1])
        damage = int(action[2])
        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()

    elif action[0] == "Defend":
        start = int(action[1])
        end = int(action[2])
        damage = int(action[3])

        if 0 <= start < len(pirate_ship) and end < len(pirate_ship):
            for x in range(start, end + 1):
                pirate_ship[x] -= damage
                if pirate_ship[x] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()

    elif action[0] == "Repair":
        index = int(action[1])
        health = int(action[2])
        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += health
            if health > maximum_health:
                health = maximum_health

    elif action[0] == "Status":
        repair_count = 0
        repair_limit = maximum_health * 0.2
        for x in pirate_ship:
            if x < repair_limit:
                repair_count += 1
        print(f"{repair_count} sections need repair.")

    command = input()

print(f"Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(warship)}")