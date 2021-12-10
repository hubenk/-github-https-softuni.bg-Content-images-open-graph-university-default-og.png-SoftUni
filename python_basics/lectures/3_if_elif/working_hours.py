hour = int(input())
day = str(input())

if 10 <= hour <= 18:
    if day in "Monday Tuesday Wednesday Thursday Friday Saturday":
        print("open")
    elif day == "Sunday":
        print("closed")
else:
    print("closed")
