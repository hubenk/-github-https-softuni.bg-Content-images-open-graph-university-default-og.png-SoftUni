def order(product, quantity):
    if product == "coffee":
        product = 1.50
    elif product == "water":
        product = 1.00
    elif product == "coke":
        product = 1.40
    elif product == "snacks":
        product = 2.00

    result = product * quantity
    return f"{result:.2f}"


type_of_product = input()
amount_of_quantity = float(input())

print(order(type_of_product, amount_of_quantity))
