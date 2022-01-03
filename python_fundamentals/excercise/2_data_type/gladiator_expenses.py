lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
shield_count = 0

for lost in range(1, lost_fights + 1):
    if lost % 2 == 0:
        expenses += helmet_price

    if lost % 3 == 0:
        expenses += sword_price

    if lost % 2 == 0 and lost % 3 == 0:
        shield_count += 1
        expenses += shield_price

        if shield_count % 2 == 0:
            expenses += armor_price


print(f"Gladiator expenses: {expenses:.2f} aureus")
