import re

orders = input()
name_regex = r"%([A-Z][a-z]+)%"
product_regex = r"<([\w]+)>"
count_regex = r"\|[1-9][0-9]*\|"
price_regex = r"[1-9]+[\.0-9]*\$"
total_income = 0

while orders != "end of shift":
    temp_price = 0

    name = re.finditer(name_regex, orders)
    for x in name:
        valid_name = x.group([1][-1])
        if valid_name:

            product = re.finditer(product_regex, orders)
            for y in product:
                valid_product = y.group([1][-1])
                if valid_product:

                    count = re.finditer(count_regex, orders)
                    for z in count:
                        valid_count = z.group()
                        valid_counts = valid_count[1:-1]
                        if valid_count:

                            price = re.finditer(price_regex, orders)
                            for q in price:
                                valid_price = q.group()
                                valid_prices = valid_price[:-1]

                                temp_sum = int(valid_counts) * float(valid_prices)
                                total_income += temp_sum
                                print(f"{valid_name}: {valid_product} - {temp_sum:.2f}")

    orders = input()

print(f"Total income: {total_income:.2f}")
