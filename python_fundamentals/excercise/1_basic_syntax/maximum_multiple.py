divisor = int(input())
boundry = int(input())
summary = 0

for x in range(boundry, 1, -1):
    summary = x / divisor
    if summary == int(summary):
        print(x)
        break
