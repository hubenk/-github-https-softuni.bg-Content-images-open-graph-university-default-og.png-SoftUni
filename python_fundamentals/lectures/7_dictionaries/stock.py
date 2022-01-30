products = input().split()
searched_products = input().split()
product_dict = {}

for x in range(0, len(products), 2):
    key = products[x]
    value = products[x + 1]
    product_dict[key] = value

for product in searched_products:
    if product in product_dict:
        print(f"We have {product_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
