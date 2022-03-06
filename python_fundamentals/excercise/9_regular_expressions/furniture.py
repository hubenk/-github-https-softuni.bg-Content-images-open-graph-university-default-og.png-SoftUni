import re

purchase = input()
regex = r"(>>(?P<furniture>[A-Za-z]+)\<<(?P<price>[0-9\.]+)!(?P<quantity>[0-9]+))"
total_money = 0
print("Bought furniture:")

while purchase != "Purchase":

    item = re.finditer(regex, purchase)

    for el in item:
        temp_money = float(el.group(3)) * float(el.group(4))
        total_money += temp_money
        print(el.group(2))

    purchase = input()

print(f"Total money spend: {total_money:.2f}")
