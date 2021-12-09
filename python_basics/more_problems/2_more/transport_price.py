kilometres = int(input())
day_night = str(input())


bus = 0.09 * kilometres

train = 0.06 * kilometres

if day_night == "day":
    taxi_day_night = 0.7 + (0.79 * kilometres)
else:
    taxi_day_night = 0.7 + (0.9 * kilometres)

if kilometres < 20:
    print(f"{taxi_day_night:.2f}")

if 20 <= kilometres < 100:
    print(f"{bus:.2f}")

if kilometres >= 100:
    print(f"{train:.2f}")