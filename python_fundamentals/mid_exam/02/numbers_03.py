initial_list = [int(number) for number in input().split()]
avg_number = sum(initial_list) / len(initial_list)
top_five = []
counter = 0

initial_list = sorted(initial_list, reverse=True)

for number in range(len(initial_list)):
    if counter < 5:
        if initial_list[number] > avg_number:
            top_five.append(initial_list[number])
            counter += 1
    else:
        break

if len(top_five) == 0:
    print("No")
else:
    print(*top_five)
