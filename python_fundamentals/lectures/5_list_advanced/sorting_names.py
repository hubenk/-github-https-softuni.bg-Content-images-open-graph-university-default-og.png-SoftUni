names = input().split(", ")
names.sort()
names = sorted(names, key=len, reverse=True)

print(names)
