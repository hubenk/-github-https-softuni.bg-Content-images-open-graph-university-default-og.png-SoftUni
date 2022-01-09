list_of_int = input().split()
numbers_to_remove = int(input())

for loop in range(numbers_to_remove):
    for number in range(len(list_of_int)):
        list_of_int[number] = int(list_of_int[number])
    min_number = min(list_of_int)
    list_of_int.remove(min_number)

for number in range(len(list_of_int)):
    list_of_int[number] = str(list_of_int[number])

print(", ".join(list_of_int))
