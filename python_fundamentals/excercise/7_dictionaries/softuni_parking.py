car_plates = int(input())
parking_database = {}

for car in range(car_plates):
    command = input().split()

    if command[0] == "register":
        if command[1] in parking_database:
            print(f"ERROR: already registered with plate number {command[2]}")
        else:
            parking_database[command[1]] = command[2]
            print(f"{command[1]} registered {command[2]} successfully")

    elif command[0] == "unregister":
        if command[1] not in parking_database:
            print(f"ERROR: user {command[1]} not found")
        else:
            parking_database.pop(command[1])
            print(f"{command[1]} unregistered successfully")

for key, value in parking_database.items():
    print(f"{key} => {value}")

