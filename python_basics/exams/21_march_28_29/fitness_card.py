budget = float(input())
gender = input()
age = int(input())
sport = input()
price = 0

if sport == "Gym":
    if gender == "m":
        price = 42
    elif gender == "f":
        price = 35

if sport == "Boxing":
    if gender == "m":
        price = 41
    elif gender == "f":
        price = 37

if sport == "Yoga":
    if gender == "m":
        price = 45
    elif gender == "f":
        price = 42

if sport == "Zumba":
    if gender == "m":
        price = 34
    elif gender == "f":
        price = 31

if sport == "Dances":
    if gender == "m":
        price = 51
    elif gender == "f":
        price = 53

if sport == "Pilates":
    if gender == "m":
        price = 39
    elif gender == "f":
        price = 37

if age <= 19:
    price *= 0.80

if price <= budget:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${price - budget:.2f} more.")