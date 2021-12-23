dancers = int(input())
points = float(input())
season = input()
place = input()

sum = dancers * points

if place == "Abroad":
    sum *= 1.5

if season == "summer":
    if place == "Abroad":
        sum *= 0.9
    else:
        sum *= 0.95
elif season == "winter":
    if place == "Abroad":
        sum *= 0.85
    else:
        sum *= 0.92

charity = sum * 0.75
money_left = (sum * 0.25) / dancers

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {money_left:.2f}")
