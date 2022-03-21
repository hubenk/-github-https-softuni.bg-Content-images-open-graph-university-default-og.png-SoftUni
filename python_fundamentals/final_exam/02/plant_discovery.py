number_of_plants = int(input())
plants = dict()

for _ in range(number_of_plants):
    plant, rarity = input().split("<->")

    if plant not in plants:
        plants[plant] = []
        plants[plant].append(int(rarity))
    else:
        plants[plant][0] = int(rarity)

command = input()
while command != "Exhibition":
    action, other = command.split(": ")

    if action == "Rate":
        plant, rating = other.split(" - ")
        if plant in plants:
            if len(plants[plant]) < 2:
                plants[plant].append(int(rating))
            else:
                plants[plant][1] += int(rating)
                plants[plant][1] /= 2
        else:
            print("error")

    elif action == "Update":
        plant, rarity = other.split(" - ")
        if plant in plants:
            plants[plant][0] = int(rarity)
        else:
            print("error")

    elif action == "Reset":
        if other in plants:
            plants[other][1] = 0
        else:
            print("error")

    command = input()

print("Plants for the exhibition:")
for key, values in sorted(plants.items(), reverse=True, key=lambda x: (x[1], x[0])):
    print(f"- {key}; Rarity: {values[0]}; Rating: {values[1]:.2f}")
