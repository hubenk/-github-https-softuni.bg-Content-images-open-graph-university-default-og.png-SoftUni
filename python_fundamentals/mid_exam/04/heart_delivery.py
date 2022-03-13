neighbourhood = [int(x) for x in input().split("@")]

jumps = input()
jump = 0

while jumps != "Love!":
    split_jumps = jumps.split()
    jump += int(split_jumps[1])

    if jump >= len(neighbourhood):
        if neighbourhood[0] == 0:
            print(f"Place {0} already had Valentine's day.")
        else:
            neighbourhood[0] -= 2
            if neighbourhood[0] == 0:
                print(f"Place {0} has Valentine's day.")
        jump = 0
    else:
        if neighbourhood[jump] == 0:
            print(f"Place {jump} already had Valentine's day.")
        else:
            neighbourhood[jump] -= 2
            if neighbourhood[jump] == 0:
                print(f"Place {jump} has Valentine's day.")

    jumps = input()

houses_count = 0
for house in neighbourhood:
    if house != 0:
        houses_count += 1

print(f"Cupid's last position was {jump}.")
if houses_count == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {houses_count} places.")