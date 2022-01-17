numbers = input().split()
rounded_list = list()

for number in numbers:
    rounded = round(float(number))
    rounded_list.append(rounded)

print(rounded_list)
