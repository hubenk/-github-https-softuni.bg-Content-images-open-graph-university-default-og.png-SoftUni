sequence_of_numbers = input().split()
int_sequence = list()

for number in sequence_of_numbers:
    int_sequence.append(int(number))

is_even = lambda x: x % 2 == 0
result = list(filter(is_even, int_sequence))

print(result)
