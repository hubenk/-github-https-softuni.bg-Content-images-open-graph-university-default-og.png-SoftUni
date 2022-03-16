rooms = input().split("|")
room_counter = 0
health = 100
bitcoins = 0

for room in rooms:
    command, number = room.split()
    room_counter += 1

    if command == "potion":
        healed_amount = 0
        if health + int(number) > 100:
            healed_amount = 100 - health
            health = 100
        else:
            health += int(number)
            healed_amount = int(number)
        print(f"You healed for {healed_amount} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += int(number)
        print(f"You found {number} bitcoins.")

    else:
        health -= int(number)
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_counter}")
            exit()

print("You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {health}")
