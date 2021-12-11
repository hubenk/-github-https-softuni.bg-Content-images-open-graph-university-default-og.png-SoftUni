budget = float(input())
category = input()
fans = int(input())
transport = 0

if category == "VIP":
    category = 499.99
elif category == "Normal":
    category = 249.99

if 1 <= fans <= 4:
    transport = budget * 0.75
elif 5 <= fans <= 9:
    transport = budget * 0.6
elif 10 <= fans <= 24:
    transport = budget * 0.5
elif 25 <= fans <= 49:
    transport = budget * 0.4
elif fans >= 50:
    transport = budget * 0.25

expenses = (category * fans) + transport
difference = abs(expenses - budget)

if budget >= expenses:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")

