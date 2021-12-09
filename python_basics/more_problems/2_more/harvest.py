from math import floor, ceil
x = int(input())
y = float(input())
z = int(input())
number_workers = int(input())

tottal_grape = floor(x * y)

litres_wine_produced = (tottal_grape * 0.4) / 2.5

wine_left = abs(floor(z - litres_wine_produced))

wine_per_worker = ceil(wine_left / number_workers)

if litres_wine_produced < z:
    print(f"It will be a tough winter! More {wine_left:.0f} liters wine needed.")

else:
    print(f"Good harvest this year! Total wine: {litres_wine_produced:.0f} liters.")
    print(f"{wine_left} liters left -> {wine_per_worker} liters per person.")
