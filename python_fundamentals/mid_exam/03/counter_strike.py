energy = int(input())
wins = 0
command = input()

while command != "End of battle":
    distance = int(command)

    if distance > energy:
        break
    elif energy <= 0:
        break

    energy -= distance
    wins += 1

    if wins % 3 == 0:
        energy += wins

    command = input()

if command == "End of battle":
    print(f"Won battles: {wins}. Energy left: {energy}")
else:
    print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
