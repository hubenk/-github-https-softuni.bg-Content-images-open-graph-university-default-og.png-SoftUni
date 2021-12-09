projection = str(input())
rows = int(input())
colons = int(input())
seats = rows * colons

if projection == "Premiere":
    sum = seats * 12.00
    print(f"{sum:.2f}")

elif projection == "Normal":
    sum = seats * 7.50
    print(f"{sum:.2f}")

elif projection == "Discount": #else:...
    sum = seats * 5.00
    print(f"{sum:.2f}")