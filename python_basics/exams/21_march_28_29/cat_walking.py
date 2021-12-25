minutes = int(input())
walks = int(input())
calories = int(input())

burned_calories = minutes * walks * 5
minimum_calories = calories * 0.5

if burned_calories >= minimum_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")
