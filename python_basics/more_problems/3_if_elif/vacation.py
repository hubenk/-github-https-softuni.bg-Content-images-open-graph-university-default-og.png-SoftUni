budget = float(input())
season = str(input())
location = ""
accommodation = ""

if season == "Summer":
    location = "Alaska"
elif season == "Winter":
    location = "Morocco"

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        budget *= 0.65
    elif season == "Winter":
        budget *= 0.45

elif 1000 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        budget *= 0.8
    elif season == "Winter":
        budget *= 0.6

elif budget > 3000:
    accommodation = "Hotel"
    budget *= 0.9

print(f"{location} - {accommodation} - {budget:.2f}")