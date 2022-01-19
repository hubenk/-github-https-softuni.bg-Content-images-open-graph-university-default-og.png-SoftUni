def only_even(even):
    if even % 2 == 0:
        return True
    return False


list_input = input().split()
even_list = list()

for number in list_input:
    if only_even(int(number)):
        even_list.append(int(number))

print(even_list)
