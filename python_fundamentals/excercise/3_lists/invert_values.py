string_number = input().split()
opposite_numbers = []

for number in range(len(string_number)):
    int_number = -int(string_number[number])
    opposite_numbers.append(int_number)

print(opposite_numbers)
