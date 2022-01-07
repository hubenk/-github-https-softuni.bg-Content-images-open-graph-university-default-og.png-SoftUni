items = input().split("|")
budget = float(input())
budget_left = budget
profit = 0
new_price = 0
new_prices_sum = 0
temp_list = list()

for x in items:
    temp_list = x.split("->")
    type = temp_list[0]
    price = float(temp_list[1])

    if type == "Clothes" and price > 50:
        continue

    elif type == "Shoes" and price > 35.00:
        continue

    elif type == "Accessories" and price > 20.50:
        continue
    else:
        if budget_left >= price:
            budget_left -= price
            new_price = round(price * 1.4, 2)
            profit += new_price - price
            new_prices_sum += new_price
        else:
            continue

    print(new_price, end=" ")
print()
new_budget = new_prices_sum + budget_left

print(f"Profit: {profit}")

if new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

