numbers = [int(x) for x in input().split()]
negative_sum = 0
positive_sum = 0

for num in numbers:
    if num > 0:
        positive_sum += num
    elif num < 0:
        negative_sum -= num

print(f"-{negative_sum}")
print(positive_sum)

if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
elif abs(negative_sum) < positive_sum:
    print("The positives are stronger than the negatives")
