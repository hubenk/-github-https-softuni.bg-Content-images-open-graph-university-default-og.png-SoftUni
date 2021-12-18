men = int(input())
women = int(input())
tables = int(input())
couples = 0

for x in range(1, men + 1):
    for y in range(1, women + 1):
        print(f"({x} <-> {y})", end=" ")
        couples += 1
        if couples == tables:
            break
    if couples == tables:
        break
