cars = int(input())
garage = dict()

for _ in range(cars):
    car, mileage, fuel = input().split("|")
    garage[car] = {}
    garage[car] = [int(mileage), int(fuel)]

command = input()
while command != "Stop":
    action = command.split(" : ")

    if action[0] == "Drive":
        car, distance, fuel = action[1], int(action[2]), int(action[3])
        if garage[car][1] >= fuel:
            garage[car][0] += distance
            garage[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if garage[car][0] >= 100000:
                print(f"Time to sell the {car}!")
                del garage[car]

        else:
            print("Not enough fuel to make that ride")

    elif action[0] == "Refuel":
        car, fuel = action[1], int(action[2])
        if garage[car][1] + fuel > 75:
            refueld = 75 - garage[car][1]
            garage[car][1] = 75
        else:
            garage[car][1] += fuel
            refueld = fuel
        print(f"{car} refueled with {refueld} liters")

    elif action[0] == "Revert":
        car, kilometres = action[1], int(action[2])

        if garage[car][0] - kilometres < 10000:
            garage[car][0] = 10000
        else:
            garage[car][0] -= kilometres
            print(f"{car} mileage decreased by {kilometres} kilometers")

    command = input()

for key, value in sorted(garage.items(), reverse=False, key=lambda x: (-x[1][0], x[0])):
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")