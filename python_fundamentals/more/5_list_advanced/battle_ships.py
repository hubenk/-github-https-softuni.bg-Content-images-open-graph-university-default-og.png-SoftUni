waves = int(input())
sea = []
sinked_ships = 0

for x in range(waves):
    ships = [int(number) for number in input().split()]
    sea.append(ships)

attacks = input().split()
for single_attack in attacks:
    row = int(single_attack[0])
    place = int(single_attack[2])
    temp_number = sea[row][place]

    if temp_number > 0:
        sea[row][place] -= 1
        if sea[row][place] == 0:
            sinked_ships += 1

print(sinked_ships)
