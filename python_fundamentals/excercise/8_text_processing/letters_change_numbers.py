characters = input().split()
final_result = list()

for sequence in characters:
    items = [x for x in sequence]
    number_list = items[1:-1]
    number = ""

    for num in number_list:
        number += str(num)

    result = 0

    if items[0].isupper():
        result += (int(number) / (ord(items[0]) - 64))
    elif items[0].islower():
        result += (int(number) * (ord(items[0]) - 96))

    if items[-1].isupper():
        result -= (ord(items[-1]) - 64)
    elif items[-1].islower():
        result += (ord(items[-1]) - 96)

    final_result.append(result)

total = sum(final_result)
print(f"{total:.2f}")
