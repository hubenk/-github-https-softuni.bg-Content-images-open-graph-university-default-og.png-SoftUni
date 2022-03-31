names_number = int(input())
names = set()

for _ in range(names_number):
    names.add(input())

print('\n'.join(names))

