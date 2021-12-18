days = int(input())
hours_per_day = int(input())
parking_tax = 0
tottal = 0
daily_sum = 0
for x in range(1, days + 1):
    for y in range(1, hours_per_day + 1):
        if x % 2 == 0 and y % 2 != 0:
            parking_tax = 2.5
        elif x % 2 != 0 and y % 2 == 0:
            parking_tax = 1.25
        else:
            parking_tax = 1

        daily_sum += parking_tax

    print(f"Day: {x} - {daily_sum:.2f} leva")
    tottal += daily_sum
    daily_sum = 0

print(f"Total: {tottal:.2f} leva")