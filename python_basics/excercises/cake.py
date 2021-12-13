width = int(input())
lenght = int(input())
cake = width * lenght


while True:
    guests = input()

    if guests == "STOP":
        print(f"{cake} pieces are left.")
        break

    cake -= int(guests)

    if cake < 0:
        cake = abs(cake)
        print(f"No more cake left! You need {cake} pieces more.")
        break



