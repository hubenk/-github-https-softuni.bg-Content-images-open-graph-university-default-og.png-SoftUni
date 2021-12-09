flowers = input()
number = int(input())
budget = int(input())
price = 0
money_left = 0

if flowers == "Roses":
    if number > 80:
        price = (number * 5) * 0.9
    else:
        price = number * 5

if flowers == "Dahlias":
    if number > 90:
        price = (number * 3.80) * 0.85
    else:
        price = number * 3.80

if flowers == "Tulips":
    if number > 80:
        price = (number * 2.80) * 0.85
    else:
        price = number * 2.80

if flowers == "Narcissus":
    if number < 120:
        price = (number * 3) * 1.15
    else:
        price = number * 3

if flowers == "Gladiolus":
    if number < 80:
        price = (number * 2.50) * 1.20
    else:
        price = number * 2.50



if budget >= price:
    money_left = budget - price
    print(f"Hey, you have a great garden with {number} {flowers} and {money_left:.2f} leva left.")

else:
    money_left = price - budget
    print(f"Not enough money, you need {money_left:.2f} leva more.")