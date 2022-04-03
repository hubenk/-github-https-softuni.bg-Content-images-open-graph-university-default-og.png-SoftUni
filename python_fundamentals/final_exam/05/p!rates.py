command = input()
cities_dict = {}

while not command == "Sail":
    city, population, gold = command.split("||")

    if city not in cities_dict:
        cities_dict[city] = []
        cities_dict[city].append(int(population))
        cities_dict[city].append(int(gold))
    elif city in cities_dict:
        cities_dict[city][0] += int(population)
        cities_dict[city][1] += int(gold)

    command = input()

command = input()

while not command == "End":
    event = command.split("=>")

    if event[0] == "Plunder":
        _, town, people, gold = event
        cities_dict[town][0] -= int(people)
        cities_dict[town][1] -= int(gold)
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities_dict[town][0] <= 0 or cities_dict[town][1] <= 0:
            del cities_dict[town]
            print(f"{town} has been wiped off the map!")

    elif event[0] == "Prosper":
        _, town, gold = event
        if int(gold) < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities_dict[town][1] += int(gold)
            print(f"{gold} gold added to the city treasury. {town} now has {cities_dict[town][1]} gold.")

    command = input()

if len(cities_dict) > 0:
    print(f"Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:")
    for key, value in cities_dict.items():
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
