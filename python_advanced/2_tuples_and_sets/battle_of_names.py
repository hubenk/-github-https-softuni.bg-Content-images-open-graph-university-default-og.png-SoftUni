from math import floor

names_number = int(input())
divider = 1
odd_set = set()
even_set = set()
odd_sum = 0
even_sum = 0

for _ in range(names_number):
    temp_sum = 0
    name = input()
    for el in name:
        temp_sum += ord(el)

    temp_sum /= divider
    temp_sum = floor(temp_sum)
    divider += 1

    if temp_sum % 2 == 0:
        even_set.add(temp_sum)
        even_sum += temp_sum
    else:
        odd_set.add(temp_sum)
        odd_sum += temp_sum

if even_sum == odd_sum:
    result = odd_set.union(even_set)
elif odd_sum > even_sum:
    result = odd_set.difference(even_set)
else:
    result = odd_set.symmetric_difference(even_set)

print(*result, sep=", ")