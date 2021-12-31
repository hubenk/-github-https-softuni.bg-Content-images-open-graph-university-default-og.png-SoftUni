budget = float(input())
price_flour_per_kg = float(input())

price_pack_of_eggs = price_flour_per_kg * 0.75
price_milk_per_liter = price_flour_per_kg * 0.25 + price_flour_per_kg
one_bread = price_pack_of_eggs + price_flour_per_kg + (price_milk_per_liter / 4)

bread_count = 0
colored_eggs_count = 0

while True:
    if budget < one_bread:
        print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.")
        break

    budget -= one_bread
    bread_count += 1
    colored_eggs_count += 3

    if bread_count % 3 == 0:
        colored_eggs_count -= (bread_count - 2)
