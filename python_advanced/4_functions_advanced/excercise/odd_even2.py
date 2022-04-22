command = input()
numbers = [int(x) for x in input().split()]

odd_even = 0 if command == "Even" else 1

result = sum([x for x in numbers if x % 2 == odd_even]) * len(numbers)

print(result)