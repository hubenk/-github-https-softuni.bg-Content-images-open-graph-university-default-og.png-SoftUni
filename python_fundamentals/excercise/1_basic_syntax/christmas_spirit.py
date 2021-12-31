quantity = int(input())
days = int(input())

ornament = 2
skirt = 5
garland = 3
lights = 15

cost = 0
spirit = 0
last_day = 0

for x in range(1, days + 1):
    if x % 11 == 0:
        quantity += 2
    if x % 5 == 0 and x % 3 == 0:
        spirit += 30
    if x % 2 == 0:
        cost += ornament * quantity
        spirit += 5
    if x % 3 == 0:
        cost += (skirt + garland) * quantity
        spirit += 13
    if x % 5 == 0:
        cost += lights * quantity
        spirit += 17

    if x % 10 == 0:
        spirit -= 20
        cost += skirt + garland + lights


    last_day = x

if last_day % 10 == 0:
    spirit -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")
