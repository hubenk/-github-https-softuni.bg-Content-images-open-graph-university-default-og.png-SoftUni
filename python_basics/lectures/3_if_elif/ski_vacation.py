days = int(input()) - 1
room = str(input())
feedback = str(input())

if room == "room for one person":
    if days < 10:
        sum = days * 18
    elif 10 <= days <= 15:
        sum = days * 18
    elif days > 15:
        sum = days * 18

elif room == "apartment":
    if days < 10:
        sum = (days * 25) * 0.7
    elif 10 <= days <= 15:
        sum = (days * 25) * 0.65
    elif days > 15:
        sum = (days * 25) * 0.5

elif room == "president apartment":
    if days < 10:
        sum = (days * 35) * 0.9
    elif 10 <= days <= 15:
        sum = (days * 35) * 0.85
    elif days > 15:
        sum = (days * 35) * 0.8

if feedback == "positive":
    tottal = sum * 1.25

elif feedback == "negative":
    tottal = sum * 0.9

print(f"{tottal:.2f}")

