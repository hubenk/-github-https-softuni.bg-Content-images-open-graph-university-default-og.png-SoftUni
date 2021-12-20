budget = float(input())
bill = 0
products = 0

while True:
    command = input()
    if command == "Stop":
        print(f"You bought {products} products for {bill:.2f} leva.")
        break

    price = float(input())

    products += 1
    if products % 3 == 0:
        price = price / 2

    bill += price

    if bill > budget:
        print("You don't have enough money!")
        print(f"You need {(bill - budget):.2f} leva!")
        break
