sequence_of_numbers = input().split()
float_list = list()
for x in sequence_of_numbers:
    float_list.append(abs(float(x)))

print(float_list)
