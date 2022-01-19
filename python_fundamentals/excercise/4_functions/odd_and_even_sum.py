def odd_even(digits):
    odd = list()
    even = list()
    for digit in digits:
        if int(digit) % 2 == 0:
            even.append(int(digit))
        else:
            odd.append(int(digit))

    sum_odd = sum(odd)
    sum_even = sum(even)

    result = f"Odd sum = {sum_odd}, Even sum = {sum_even}"
    return result


single_number = input()
print(odd_even(single_number))
