budget = float(input())
season = str(input())
car = ""
class_car = ""
rent = 0

if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        car = "Cabrio"
        rent = budget * 0.35
    elif season == "Winter":
        car = "Jeep"
        rent = budget * 0.65

elif 100 < budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        car = "Cabrio"
        rent = budget * 0.45
    elif season == "Winter":
        car = "Jeep"
        rent = budget * 0.8

elif budget > 500:
    class_car = "Luxury class"
    car = "Jeep"
    rent = budget * 0.9

print(class_car)
print(f"{car} - {rent:.2f}")