needed_money = int(input())
average_cash = 0
cash_count = 0
average_card = 0
card_count = 0
count = 0
while True:
    sum = input()
    count += 1

    if sum == "End":
        print("Failed to collect required money for charity.")
        break
    if count % 2 == 0:
        if int(sum) < 10:
            print("Error in transaction!")
        elif int(sum) >= 10:
            average_card += int(sum)
            card_count += 1
            print("Product sold!")

    else:
        if int(sum) > 100:
            print("Error in transaction!")
        else:
            average_cash += int(sum)
            cash_count += 1
            print("Product sold!")

    if average_card + average_cash >= needed_money:
        avg_card = average_card / card_count
        avg_cash = average_cash / cash_count
        print(f"Average CS: {avg_cash:.2f}")
        print(f"Average CC: {avg_card:.2f}")
        break



