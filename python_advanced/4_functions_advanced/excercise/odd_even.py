command = input()
numbers = [int(x) for x in input().split()]

if command == "Odd":
    odd = sum([x for x in numbers if x % 2 != 0]) * len(numbers)
    print(odd)
elif command == "Even":
    even = sum([x for x in numbers if x % 2 == 0]) * len(numbers)
    print(even)