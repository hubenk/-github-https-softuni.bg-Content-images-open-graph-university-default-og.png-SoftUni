from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque([int(x) for x in input().split(", ")])
milkshakes = 0
got_milkshake = False

while True:
    if chocolates[-1] <= 0:
        chocolates.pop()
        if len(chocolates) == 0:
            break
    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        if len(cups_of_milk) == 0:
            break

    if chocolates[-1] == cups_of_milk[0]:
        chocolates.pop()
        cups_of_milk.popleft()
    else:
        cups_of_milk.rotate()
        chocolates[-1] -= 5

    milkshakes += 1
    if milkshakes == 5:
        got_milkshake = True
        break
    elif len(chocolates) == 0 or len(cups_of_milk) == 0:
        break

if got_milkshake:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if len(chocolates) == 0:
    print("Chocolate: empty")
else:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")

if len(cups_of_milk) == 0:
    print("Milk: empty")
else:
    print(f"Milk: {', '.join([str(x) for x in cups_of_milk])}")
