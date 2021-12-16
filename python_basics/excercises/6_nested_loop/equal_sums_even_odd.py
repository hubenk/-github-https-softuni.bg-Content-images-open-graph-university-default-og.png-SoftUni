number1 = int(input())
number2 = int(input())


for x in range(number1, number2 + 1):
    sum_even = 0
    sum_odd = 0
    x_string = str(x)
    for index, digit in enumerate(x_string):
        if index % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)

    if sum_odd == sum_even:
        print(x, end=" ")

