from math import floor
string = [x for x in input().split()]
temp_numbers = []

for x in string:
    if (x.strip("-")).isdigit():
        temp_numbers.append(int(x))
    else:
        temp_total = 0
        if x == "+":
            for y in temp_numbers:
                temp_total += y
        elif x == "-":
            temp_total = temp_numbers[0]
            for y in temp_numbers[1:]:
                temp_total -= y
        elif x == "*":
            temp_total = temp_numbers[0]
            for y in temp_numbers[1:]:
                temp_total *= y
        elif x == "/":
            temp_total = temp_numbers[0]
            for y in temp_numbers[1:]:
                temp_total /= y
            temp_total = floor(temp_total)

        temp_numbers = [temp_total]

print(*temp_numbers)
