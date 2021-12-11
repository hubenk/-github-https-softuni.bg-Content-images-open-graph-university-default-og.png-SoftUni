hrizantema = int(input())
roses = int(input())
tulips = int(input())
season = str(input())
holiday = str(input())

hriza_price = 0
ros_price = 0
tul_price = 0

if season == "Spring" or season == "Summer":
    hriza_price = 2
    ros_price = 4.1
    tul_price = 2.5
elif season == "Winter" or season == "Autumn":
    hriza_price = 3.75
    ros_price = 4.5
    tul_price = 4.15

buket = (hrizantema * hriza_price) + (ros_price * roses) + (tul_price * tulips)

if holiday == "Y":
    buket *= 1.15

if season == "Spring" and tulips > 7:
    buket *= 0.95

elif season == "Winter" and roses >= 10:
    buket *= 0.9

if (hrizantema + roses + tulips) > 20:
    buket *= 0.8

sum = buket + 2

print(f"{sum:.2f}")