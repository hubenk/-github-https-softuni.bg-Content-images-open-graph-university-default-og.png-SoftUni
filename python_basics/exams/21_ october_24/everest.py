camp = 5364
days = 1

while True:
    command = input()

    if command == "Yes":
        days += 1

    if command == "END" or days > 5:
        print("Failed!")
        print(f"{camp}")
        break


    else:
        pass

    metres = int(input())
    camp += metres

    if camp >= 8848:
        print(f"Goal reached for {days} days!")
        break


