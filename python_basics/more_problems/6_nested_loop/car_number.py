start_number = int(input())
end_number = int(input())

for x in range(start_number, end_number + 1):
    for y in range(start_number, end_number + 1):
        for z in range(start_number, end_number + 1):
            for q in range(start_number, end_number + 1):
                if x > q:
                    if (y + z) % 2 == 0:
                        if x % 2 == 0 and q % 2 != 0:
                            print(f"{x}{y}{z}{q}", end=" ")
                        elif x % 2 != 0 and q % 2 == 0:
                            print(f"{x}{y}{z}{q}", end=" ")
