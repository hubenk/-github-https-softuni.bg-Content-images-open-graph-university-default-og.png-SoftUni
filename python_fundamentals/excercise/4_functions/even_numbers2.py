def is_even(numbers):
    return lambda x: x % 2 == 0


sequence_of_numbers = input().split()
int_sequence = list()

for number in sequence_of_numbers:
    int_sequence.append(int(number))

result = list(filter(is_even(int_sequence), int_sequence))

print(result)
