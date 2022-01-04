lines = int(input())
liters_in_tank = 0
total_water = 0
for x in range(lines):
    liters_water = int(input())
    total_water += liters_water
    if total_water > 255:
        print("Insufficient capacity!")
        total_water -= liters_water
    else:
        liters_in_tank += liters_water

print(liters_in_tank)
