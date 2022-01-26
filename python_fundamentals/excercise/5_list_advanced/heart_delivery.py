houses = [int(house) for house in input().split("@")]
command = input().split()
last_index = 0

while command[0] != "Love!":

    temp_index = last_index + int(command[1])

    if temp_index < len(houses) and houses[temp_index] == 0:
        print(f"Place {temp_index} already had Valentine's day.")
        last_index = temp_index
        command = input().split()
        continue

    if temp_index >= len(houses):
        temp_index = 0
        if houses[temp_index] == 0:
            print(f"Place {temp_index} already had Valentine's day.")
            last_index = temp_index
            command = input().split()
            continue
        else:
            houses[temp_index] -= 2
    else:
        houses[temp_index] -= 2

    if houses[temp_index] <= 0:
        houses[temp_index] = 0
        print(f"Place {temp_index} has Valentine's day.")

    last_index = temp_index
    command = input().split()

print(f"Cupid's last position was {last_index}.")
if houses.count(0) == len(houses):
    print("Mission was successful.")
else:
    failed = len(houses) - houses.count(0)
    print(f"Cupid has failed {failed} places.")