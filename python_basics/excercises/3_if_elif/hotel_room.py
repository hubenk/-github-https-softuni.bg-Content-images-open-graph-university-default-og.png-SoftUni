month = str(input())
nights = int(input())
studio = 0
apartment = 0

if month == "May" or month == "October":
    apartment = nights * 65
    if 14 >= nights > 7:
        studio = (50 * nights) * 0.95
    elif nights > 14:
        studio = (50 * nights) * 0.70
    else:
        studio = 50 * nights

elif month == "June" or month == "September":
    apartment = nights * 68.70
    if nights > 14:
        studio = (nights * 75.20) * 0.80
    else:
        studio = nights * 75.20

elif month == "July" or month == "August":
    apartment = nights * 77
    studio = nights * 76

if nights > 14:
    apartment *= 0.90

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")