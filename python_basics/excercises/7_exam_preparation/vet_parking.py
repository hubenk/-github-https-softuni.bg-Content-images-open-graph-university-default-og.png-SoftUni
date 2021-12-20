days = int(input())
hours = int(input())
total = 0
cost = 0

for x in range(1, days + 1):
    for y in range(1, hours + 1):
        if x % 2 == 0:
            if y % 2 != 0:
                cost += 2.5
            else:
                cost += 1
        elif x % 2 != 0:
            if y % 2 == 0:
                cost += 1.25
            else:
                cost +=1
    print(f"Day: {x} - {cost:.2f} leva")
    total += cost
    cost = 0
print(f"Total: {total:.2f} leva")