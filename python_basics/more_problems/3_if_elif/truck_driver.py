season = str(input())
km_per_month = float(input())
km_per_season = 0

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        km_per_season = (km_per_month * 0.75) * 4
    elif season == "Summer":
        km_per_season = (km_per_month * 0.9) * 4
    elif season == "Winter":
        km_per_season = (km_per_month * 1.05) * 4

elif 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        km_per_season = (km_per_month * 0.95) * 4
    elif season == "Summer":
        km_per_season = (km_per_month * 1.1) * 4
    elif season == "Winter":
        km_per_season = (km_per_month * 1.25) * 4

else:
    km_per_season = (km_per_month * 1.45) * 4

sum = km_per_season * 0.9

print(f"{sum:.2f}")