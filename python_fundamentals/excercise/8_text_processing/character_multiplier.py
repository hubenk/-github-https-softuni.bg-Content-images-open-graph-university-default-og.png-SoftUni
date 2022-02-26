def multiplication(short, long):
    total_sum = 0
    for index in range(len(short)):
        total_sum += (ord(short[index]) * ord(long[index]))
    if short != long:
        for index in range(len(short), len(long)):
            total_sum += (ord(long[index]))

    return total_sum


str1, str2 = input().split()

if len(str1) > len(str2):
    print(multiplication(str2, str1))
elif len(str1) < len(str2):
    print(multiplication(str1, str2))
else:
    print(multiplication(str1, str2))
