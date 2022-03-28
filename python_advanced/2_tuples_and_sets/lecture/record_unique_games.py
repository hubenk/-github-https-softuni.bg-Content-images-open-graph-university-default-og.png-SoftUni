names_number = int(input())
names = set()

for _ in range(names_number):
    name = input()
    names.add(name)

print('\n'.join(names))
