input = int(input())

for x in range(1, input + 1):
    print(("* " * x).center(input * 2))
for y in range(input - 1, 0, -1):
    print(("* " * y).center(input * 2))
