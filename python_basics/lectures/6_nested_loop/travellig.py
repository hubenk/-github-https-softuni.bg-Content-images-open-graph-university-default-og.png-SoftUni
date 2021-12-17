saved_money = 0

while True:
    destination = input()
    if destination == "End":
        break

    budget = float(input())
    while saved_money < budget:
        money = float(input())
        saved_money += money
        if saved_money >= budget:
            print(f"Going to {destination}!")
            saved_money = 0
            break