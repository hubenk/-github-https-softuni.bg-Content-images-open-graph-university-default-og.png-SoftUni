products = input().split()
orders = {}

while products[0] != "buy":

    if products[0] not in orders:
        orders[products[0]] = [float(products[1]), float(products[2])]
    else:
        orders[products[0]][0] = float(products[1])
        orders[products[0]][1] += float(products[2])

    products = input().split()

for order in orders:
    num1 = orders[order][0]
    num2 = orders[order][1]
    prices = num1 * num2
    print(f"{order} -> {prices:.2f}")