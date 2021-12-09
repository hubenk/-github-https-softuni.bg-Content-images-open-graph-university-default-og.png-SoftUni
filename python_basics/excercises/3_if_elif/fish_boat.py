budget = int(input())
season = str(input())
fisherman = int(input())
rent = 0

if season == "Spring":
    if fisherman <= 6:
        rent = 3000 * 0.9
    elif 7 < fisherman <= 11: # fisherman <= 11
        rent = 3000 * 0.85
    elif fisherman >= 12:
        rent = 3000 * 0.75

elif season == "Summer" or season == "Autumn":
    if fisherman <= 6:
        rent = 4200 * 0.9
    elif 7 < fisherman <= 11:  # fisherman <= 11
        rent = 4200 * 0.85
    elif fisherman >= 12:
        rent = 4200 * 0.75

elif season == "Winter":
    if fisherman <= 6:
        rent = 2600 * 0.9
    elif 7 < fisherman <= 11: # fisherman <= 11
        rent = 2600 * 0.85
    elif fisherman >= 12:
        rent = 2600 * 0.75

if season != "Autumn" and fisherman % 2 == 0:
    rent *= 0.95

if budget >= rent:
    total = budget - rent
    print(f"Yes! You have {total:.2f} leva left.")

elif budget < rent:
    total = rent - budget
    print(f"Not enough money! You need {total:.2f} leva.")


