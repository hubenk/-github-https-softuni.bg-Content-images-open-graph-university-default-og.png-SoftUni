import sys

list_of_str = input().split()
numbers_to_remove = int(input())

for loop in range(numbers_to_remove):
    min_number = sys.maxsize
    for number in range(len(list_of_str)):
        if int(list_of_str[number]) < min_number:
            min_number = int(list_of_str[number])
    list_of_str.remove(str(min_number))


print(", ".join(list_of_str))
