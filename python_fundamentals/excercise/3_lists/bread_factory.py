string = input().split("|")
energy = 100
coins = 100
event = list()
gained_energy = 0

for x in string:
    initial_energy = energy
    event = x.split("-")

    if event[0] == "rest":
        energy += int(event[1])
        if energy > 100:
            energy = 100
        gained_energy = energy - initial_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event[0] == "order":
        if energy >= 30:
            energy -= 30
            coins += int(event[1])
            print(f"You earned {event[1]} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins - int(event[1]) >= 0:
            coins -= int(event[1])
            print(f"You bought {event[0]}.")

        else:
            print(f"Closed! Cannot afford {event[0]}.")
            exit()


print("Day completed!")
print(f"Coins: {coins}")
print(f"Energy: {energy}")

