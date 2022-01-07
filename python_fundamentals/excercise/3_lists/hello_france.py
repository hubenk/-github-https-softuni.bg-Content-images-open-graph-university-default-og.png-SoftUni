items = input().split("|")
budget = float(input())
budget_left = budget
profit = 0
new_price = 0
new_prices = list()
separated_items = list()
temp_list = list()

for x in items:
    separated_items = x.replace("->", " ")
    temp_item = ""
    temp_list.clear()

    for item in separated_items:
        if item != " ":
            temp_item += item
        else:
            temp_list.append(temp_item)
            temp_item = ""
    temp_list.append(temp_item)

    if temp_list[0] == "Clothes" and float(temp_list[1]) <= 50:
        if float(temp_list[1]) <= budget_left:
            budget_left -= float(temp_list[1])
            new_price = float(temp_list[1]) * 1.4
            profit += new_price - float(temp_list[1])
            new_prices.append(new_price)

    elif temp_list[0] == "Shoes" and float(temp_list[1]) <= 35.00:
        if float(temp_list[1]) <= budget_left:
            budget_left -= float(temp_list[1])
            new_price = float(temp_list[1]) * 1.4
            profit += new_price - float(temp_list[1])
            new_prices.append(new_price)

    elif temp_list[0] == "Accessories" and float(temp_list[1]) <= 20.50:
        if float(temp_list[1]) <= budget_left:
            budget_left -= float(temp_list[1])
            new_price = float(temp_list[1]) * 1.4
            profit += new_price - float(temp_list[1])
            new_prices.append(new_price)


new_prices_sum = sum(new_prices)
new_budget = new_prices_sum + budget_left
formatted_list = [round(elem, 2) for elem in new_prices]

print(" ".join(map(str, formatted_list)))
print(f"Profit: {profit:.2f}")

if new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

