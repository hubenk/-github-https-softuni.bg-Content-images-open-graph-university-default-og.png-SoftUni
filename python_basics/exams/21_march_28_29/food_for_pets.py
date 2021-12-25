days = int(input())
food = float(input())
dog_food = 0
cat_food = 0
biscuits = 0

for x in range(1, days + 1):
    dog = int(input())
    cat = int(input())

    dog_food += dog
    cat_food += cat

    if x % 3 == 0:
        biscuits += (dog + cat) * 0.10

eaten_food = ((dog_food + cat_food) / food) * 100
eaten_from_dog = dog_food / (dog_food + cat_food) * 100
eaten_from_cat = cat_food / (dog_food + cat_food) * 100

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{eaten_food:.2f}% of the food has been eaten.")
print(f"{eaten_from_dog:.2f}% eaten from the dog.")
print(f"{eaten_from_cat:.2f}% eaten from the cat.")