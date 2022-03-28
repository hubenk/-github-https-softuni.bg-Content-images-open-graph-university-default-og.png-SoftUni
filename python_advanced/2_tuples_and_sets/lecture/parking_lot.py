cars_number = int(input())
parking = set()

for _ in range(cars_number):
    direction, number = input().split(", ")

    if direction == "IN":
        parking.add(number)
    elif direction == "OUT":
        if number in parking:
            parking.remove(number)

if len(parking) == 0:
    print("Parking Lot is Empty")
else:
    print('\n'.join(parking))
