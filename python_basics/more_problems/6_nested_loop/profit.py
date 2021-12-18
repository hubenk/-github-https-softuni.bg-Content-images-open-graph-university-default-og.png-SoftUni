coin_1lv = int(input())
coin_2lv = int(input())
banknote_5lv = int(input())
tottal_sum = int(input())
sum_x = 0
sum_y = 0
sum_z = 0

for x in range(coin_1lv + 1):
    sum_x = x * 1
    for y in range(coin_2lv + 1):
        sum_y = y * 2
        for z in range(banknote_5lv + 1):
            sum_z = z * 5
            if sum_x + sum_y + sum_z == tottal_sum:
                print(f"{x} * 1 lv. + {y} * 2 lv. + {z} * 5 lv. = {tottal_sum} lv.")
                continue
