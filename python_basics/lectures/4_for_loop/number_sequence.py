import sys

number = int(input())

smallest = sys.maxsize
biggest = -sys.maxsize

for x in range(number):
    num = int(input())

    if num > biggest:
        biggest = num
    if num < smallest:
        smallest = num

print(f"Max number: {biggest}")
print(f"Min number: {smallest}")