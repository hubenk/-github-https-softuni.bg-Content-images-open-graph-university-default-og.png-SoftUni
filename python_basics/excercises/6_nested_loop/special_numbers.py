input_number = int(input())

for x in range(1111, 9999 + 1):
    special_number_is = True
    x_string = str(x)
    for number in x_string:
        if int(number) == 0 or input_number % int(number) != 0:
            special_number_is = False
            break
    if special_number_is:
        print(x, end = " ")
