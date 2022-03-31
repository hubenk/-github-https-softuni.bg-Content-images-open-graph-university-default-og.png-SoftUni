from collections import deque

bees = deque([int(x) for x in input().split()])
honey = [int(x) for x in input().split()]
symbol = input().split()
index_bees = 0
index_honey = -1
collected = []
honey_made = 0

while True:
    if bees[0] > honey[-1]:
        honey.pop()
    else:
        collected.append([bees[0], honey[-1]])
        bees.popleft()
        honey.pop()

    if len(bees) == 0 or len(honey) == 0:
        break
if len(collected) > 0:
    for index in range(len(collected)):
        bee, sweet = collected[index][0], collected[index][1]
        result = 0
        if symbol[index] == "+":
            result = bee + sweet
        elif symbol[index] == "-":
            result = abs(bee - sweet)
        elif symbol[index] == "*":
            result = bee * sweet
        elif symbol[index] == "/":
            result = bee / sweet

        honey_made += result

print(f"Total honey made: {honey_made}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if honey:
    print(f"Nectar left: {', '.join([str(x) for x in honey])}")

