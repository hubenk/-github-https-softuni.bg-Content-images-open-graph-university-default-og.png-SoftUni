number = int(input())
type = str(input())
delivery = str(input())
price = 0
discount = 0


if type == "90X130":
    price = 110
    if number > 60:
        discount = 0.92
    elif number > 30:
        discount = 0.95
    else:
        discount = 1

elif type == "100X150":
    price = 140
    if number > 80:
        discount = 0.9
    elif number > 40:
        discount = 0.94
    else:
        discount = 1

elif type == "130X180":
    price = 190
    if number > 50:
        discount = 0.88
    elif number > 20:
        discount = 0.93
    else:
        discount = 1
elif type == "200X300":
    price = 250
    if number > 50:
        discount = 0.86
    elif number > 25:
        discount = 0.91
    else:
        discount = 1

sum = (price * number) * discount

if delivery == "With delivery":
    sum += 60

if number > 99:
   sum *= 0.96


if number < 10:
    print("Invalid order")
else:
    print(f"{sum:.2f} BGN")
