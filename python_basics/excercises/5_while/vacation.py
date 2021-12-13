vacation_price = float(input())
balance = float(input())
spend_days = 0
save_days = 0
total_days = 0

while True:
    expense_behaviour = input()
    daily_money = float(input())
    total_days += 1

    if expense_behaviour == "spend":
        spend_days += 1
        balance -= daily_money
        if balance < 0:
            balance = 0
        if spend_days == 5:
            print("You can't save the money.")
            print(total_days)
            break

    if expense_behaviour == "save":
        balance += daily_money
        spend_days = 0

    if balance >= vacation_price:
        print(f"You saved the money for {total_days} days.")
        break




