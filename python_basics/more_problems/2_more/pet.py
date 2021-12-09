from math import ceil, floor
days = int(input())
food = int(input())
dog = float(input())
cat = float(input())
turtle = float(input())

turtle /= 1000

needed_food = days * (dog + cat + turtle)

enough = floor(food - needed_food)
not_enough = ceil(needed_food - food)

if food >= needed_food:
    print(f"{enough} kilos of food left.")

else:
    print(f"{not_enough} more kilos of food are needed.")
