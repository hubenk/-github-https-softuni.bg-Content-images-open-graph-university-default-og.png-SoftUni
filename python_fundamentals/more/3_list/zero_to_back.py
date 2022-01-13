single_string = input().split(", ")
count_zeros = 0
int_list = list()

for zero in single_string:
    if int(zero) == 0:
        count_zeros += 1

for remove_zero in range(count_zeros):
    single_string.remove("0")

for add_zeros in range(count_zeros):
    single_string.append("0")

for new_list in single_string:
    int_list.append(int(new_list))

print(int_list)
