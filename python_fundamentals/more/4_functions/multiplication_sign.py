def multiplication(num1, num2, num3):
    if num1 == 0 or num2 == 0 or num3 == 0:
        return "zero"
    elif num1 < 0 or num2 < 0 or num3 < 0:
        count = 0
        if num1 < 0:
            count += 1
        if num2 < 0:
            count += 1
        if num3 < 0:
            count += 1
        if count != 2:
            return "negative"
    return "positive"


number1 = int(input())
number2 = int(input())
number3 = int(input())

print(multiplication(number1, number2, number3))
