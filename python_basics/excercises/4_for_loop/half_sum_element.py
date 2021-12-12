import sys

entry = int(input())
max_number = -sys.maxsize
sum_numbers = 0

for x in range(entry):
    num = int(input())
    sum_numbers += num
    if num > max_number:
        max_number = num


if max_number == (sum_numbers - max_number):
    print("Yes")
    print(f"Sum = {max_number}")
else:
    diff = abs(max_number - (sum_numbers - max_number))
    print("No")
    print(f"Diff = {diff}")
