input_number = int(input())
special_number = 0

for x in range(1111, 9999):
    number1 = x // 10000
    number2 = x // 1000
    number3 = x // 100
    number4 = x // 10

    if input_number // number1 == 0 and input_number // number2 == 0 and input_number // number3 == 0 and input_number // number4 == 0:
        print(special_number, end = " ")
    