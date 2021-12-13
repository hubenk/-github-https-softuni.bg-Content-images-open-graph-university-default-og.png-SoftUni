months = int(input())
electricity = 0
water = 0
internet = 0
others = 0

for x in range(months):
    electro = float(input())

    electricity += electro
    water += 20
    internet += 15
    others += (electro + 20 + 15) * 1.2

avg = (electricity + water + internet + others) / months

print(f"Electricity: {electricity:.2f}")
print(f"Water: {water:.2f}")
print(f"Internet: {internet:.2f}")
print(f"Other: {others:.2f}")
print(f"Average: {avg:.2f}")