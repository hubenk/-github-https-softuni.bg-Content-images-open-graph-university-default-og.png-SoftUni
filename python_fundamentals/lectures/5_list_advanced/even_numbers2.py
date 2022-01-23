single_string = input().split(", ")
even_list = []
for index, number in enumerate(single_string):
    if int(number) % 2 == 0:
        even_list.append(index)

print(even_list)
