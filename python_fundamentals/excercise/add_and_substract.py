def sum_numbers(num1, num2):
    return num1 + num2


def substract(total, num3):
    return total - num3


def add_and_substract(numb1, numb2, numb3):
    result = substract(sum_numbers(numb1, numb2), numb3)
    return result


number1 = int(input())
number2 = int(input())
number3 = int(input())

print(add_and_substract(number1, number2, number3))
