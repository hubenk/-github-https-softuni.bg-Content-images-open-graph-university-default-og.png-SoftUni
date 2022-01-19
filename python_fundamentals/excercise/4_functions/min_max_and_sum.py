values = input().split()

int_values = [int(number) for number in values]

min_number = min(int_values)
max_number = max(int_values)
sum_numbers = sum(int_values)

print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_numbers}")
