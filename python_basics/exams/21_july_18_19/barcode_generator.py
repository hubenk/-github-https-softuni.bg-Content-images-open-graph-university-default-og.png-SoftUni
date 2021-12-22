entry = int(input())
exit = int(input())

entry_1 = entry // 1000
entry_2 = (entry // 100) % 10
entry_3 = (entry // 10) % 10
entry_4 = entry % 10
exit_1 = exit // 1000
exit_2 = (exit // 100) % 10
exit_3 = (exit // 10) % 10
exit_4 = exit % 10

for x in range(entry_1, exit_1 + 1):
    if x % 2 != 0:
        for y in range(entry_2, exit_2 + 1):
            if y % 2 != 0:
                for z in range(entry_3, exit_3 + 1):
                    if z % 2 != 0:
                        for q in range(entry_4, exit_4 + 1):
                            if q % 2 != 0:

                                print(f"{x}{y}{z}{q}", end=" ")


