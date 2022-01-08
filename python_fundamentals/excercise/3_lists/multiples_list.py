number = int(input())
loop = int(input())

current_list = []

for x in range(1, loop + 1):
    current_list.append(x * number)

print(current_list)
