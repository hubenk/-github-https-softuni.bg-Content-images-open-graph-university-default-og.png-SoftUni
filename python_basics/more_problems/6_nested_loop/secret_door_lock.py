max_x = int(input())
max_y = int(input())
max_z = int(input())

for x in range(1, max_x + 1):
    if x % 2 == 0:
        for y in range(1, max_y + 1):
            if y in (2,3,5,7):
                for z in range(1, max_z +1):
                    if z % 2 == 0:
                        print(f"{x} {y} {z}")
