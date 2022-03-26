petrol_pumps = int(input())
tank = 0
full_circle = 0
petrol_circle = []
pump_count = 0
start_index = 0

for x in range(petrol_pumps):
    petrol, distance = [int(x) for x in input().split()]
    petrol_circle.append([petrol, distance])

while True:
    if pump_count == petrol_pumps:
        pump_count = 0

    petrol, distance = petrol_circle[pump_count]
    tank += petrol
    full_circle += 1

    if tank - distance < 0:
        tank = 0
        full_circle = 0
        start_index = pump_count + 1
    else:
        tank -= distance

    if full_circle == petrol_pumps:
        break

    pump_count += 1

print(start_index)