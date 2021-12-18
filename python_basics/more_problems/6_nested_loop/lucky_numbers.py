n = int(input())

for x in range(1, n):
    if x < 10:
        for y in range(1, n):
            if y < 10:
                for z in range(1, n):
                    if z < 10:
                        for q in range(1, n):
                            if q < 10:
                                if x + y == z + q and n % (x+y) == 0:
                                    print(f"{x}{y}{z}{q}", end=" ")
