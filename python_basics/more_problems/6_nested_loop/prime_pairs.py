pair_start_1 = int(input())
pair_start_2 = int(input())
end_1 = int(input()) + pair_start_1
end_2 = int(input()) + pair_start_2
pair = 0

for x in range(pair_start_1, end_1 + 1):
    for y in range(pair_start_2, end_2 + 1):
        pair = f"{x}{y}"
        if x % 2 != 0 and y % 2 != 0 and x % 3 != 0 and y % 3 != 0 and x % 5 !=0 and y % 5 != 0 and x % 7 != 0 and y % 7 != 0:
            print(f"{x}{y}")
