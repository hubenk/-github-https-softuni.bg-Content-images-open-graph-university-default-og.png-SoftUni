fruit = input()
set = input()
number_of_sets = int(input())
price = 0

if fruit == "Watermelon":
    if set == "small":
        price = 56 * 2
    elif set == "big":
        price = 28.70 * 5

if fruit == "Mango":
    if set == "small":
        price = 36.66 * 2
    elif set == "big":
        price = 19.60 * 5

if fruit == "Pineapple":
    if set == "small":
        price = 42.10 * 2
    elif set == "big":
        price = 24.80 * 5

if fruit == "Raspberry":
    if set == "small":
        price = 20 * 2
    elif set == "big":
        price = 15.20 * 5

total = number_of_sets * price

if 400 <= total <= 1000:
    total *= 0.85
elif total > 1000:
    total *= 0.50

print(f"{total:.2f} lv.")
