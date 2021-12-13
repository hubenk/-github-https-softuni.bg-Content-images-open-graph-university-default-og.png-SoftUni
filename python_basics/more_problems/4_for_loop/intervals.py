number_of_intervals = int(input())
interval_0_9 = 0
interval_10_19 = 0
interval_20_29 = 0
interval_30_39 = 0
interval_40_50 = 0
invalid_number = 0
result = 0

for x in range(number_of_intervals):
    number = int(input())
    if number < 0 or number > 50:
        result /= 2
        invalid_number += 1
    elif 0 <= number <= 9:
        result += number * 0.2
        interval_0_9 += 1
    elif number <= 19:
        result += number * 0.3
        interval_10_19 += 1
    elif number <= 29:
        result += number * 0.4
        interval_20_29 += 1
    elif number <= 39:
        result += 50
        interval_30_39 += 1
    elif number <= 50:
        result += 100
        interval_40_50 += 1

percnt09 = interval_0_9 / number_of_intervals * 100
percnt19 = interval_10_19 / number_of_intervals * 100
percnt29 = interval_20_29 / number_of_intervals * 100
percnt39 = interval_30_39 / number_of_intervals * 100
percnt50 = interval_40_50 / number_of_intervals * 100
percntinv = invalid_number / number_of_intervals * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {percnt09:.2f}%")
print(f"From 10 to 19: {percnt19:.2f}%")
print(f"From 20 to 29: {percnt29:.2f}%")
print(f"From 30 to 39: {percnt39:.2f}%")
print(f"From 40 to 50: {percnt50:.2f}%")
print(f"Invalid numbers: {percntinv:.2f}%")
