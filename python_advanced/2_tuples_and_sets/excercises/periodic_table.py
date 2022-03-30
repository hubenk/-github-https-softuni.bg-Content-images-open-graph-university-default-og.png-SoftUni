elements_number = int(input())
elements = set()

for _ in range(elements_number):
    temp_el = input().split()
    for el in temp_el:
        elements.add(el)

print('\n'.join(elements))

