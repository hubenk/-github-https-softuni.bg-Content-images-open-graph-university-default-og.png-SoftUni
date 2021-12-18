number_1 = int(input())
number_2 = int(input())
number_3 = int(input())


for x in range(2,number_1 + 1, 2):
    for y in range(2, number_2 + 1):
        for z in range(2, number_3 + 1, 2):
            if y == 2 or y == 3 or y == 5 or y == 7:
                print(f"{x} {y} {z}")


