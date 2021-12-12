number = int(input())
sum = 0
sum2 = 0
for x in range(number):
    num = int(input())
    sum += num

for x in range(number):
    num = int(input())
    sum2 += num

if sum == sum2:
    print(f"Yes, sum = {sum}")

else:
    total = abs(sum-sum2)
    print(f"No, diff = {total}")
