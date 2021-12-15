number = int(input())
total = 0

for x in range(number):
    n = int(input())
    total += n

avg = total / number
print(f"{avg:.2f}")

