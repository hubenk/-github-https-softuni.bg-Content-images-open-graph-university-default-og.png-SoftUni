prices_no_vat = input()
no_vat_price = 0

while True:
    if prices_no_vat == "special" or prices_no_vat == "regular":
        break
    price = float(prices_no_vat)

    if price < 0:
        print("Invalid price!")
    else:
        no_vat_price += price

    prices_no_vat = input()

price_with_vat = no_vat_price * 1.2
price_no_disc = price_with_vat
if prices_no_vat == "special":
    price_with_vat *= 0.9

vat = price_no_disc - no_vat_price

if price_with_vat == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {no_vat_price:.2f}$")
    print(f"Taxes: {vat:.2f}$")
    print("-----------")
    print(f"Total price: {price_with_vat:.2f}$")