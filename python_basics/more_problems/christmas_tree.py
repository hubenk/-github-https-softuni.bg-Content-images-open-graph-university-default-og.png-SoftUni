number = int(input())

for x in range(number + 1):
    print(("*" * x + " | " + "*" * x).center(number * 2 + 3))
