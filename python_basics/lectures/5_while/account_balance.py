balance = 0

while True:
    deposit = input()

    if deposit == "NoMoreMoney":
        break

    elif float(deposit) < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {float(deposit):.2f}")
    balance += float(deposit)

print(f"Total: {balance:.2f}")
