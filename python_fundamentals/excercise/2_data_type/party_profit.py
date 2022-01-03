from math import floor

group_size = int(input())
days = int(input())
coins = 0

for days in range(1, days + 1):

    if days % 15 == 0:
        group_size += 5
    if days % 10 == 0:
        group_size -= 2
    if days % 3 == 0:
        coins -= group_size * 3
    if days % 5 == 0:
        coins += 20 * group_size
        if days % 3 == 0:
            coins -= group_size * 2

    coins += 50 - (group_size * 2)

coins_per_companion = floor(coins / group_size)

print(f"{group_size} companions received {coins_per_companion} coins each.")
