age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
saved_money = 0
toy_number = 0
brother = 0
tottal_saved_money = 0

for x in range(1,age + 1):
    if x % 2 != 0:
        toy_number += 1
    else:
        saved_money += 10
        tottal_saved_money += saved_money - 1


all_toy = toy_price * toy_number
all_saved = tottal_saved_money + all_toy
diff = abs(washing_machine_price - all_saved)

if all_saved >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")

