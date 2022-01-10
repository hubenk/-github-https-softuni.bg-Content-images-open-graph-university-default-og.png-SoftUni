orders = int(input())
total_price = 0
single_order = 0

while orders != 0:

    capsule = float(input())
    days = int(input())
    capsules_counter = int(input())

    single_order = capsule * days * capsules_counter
    total_price += single_order
    print(f"The price for the coffee is: ${single_order:.2f}")
    orders -= 1

print(f"Total: ${total_price:.2f}")
