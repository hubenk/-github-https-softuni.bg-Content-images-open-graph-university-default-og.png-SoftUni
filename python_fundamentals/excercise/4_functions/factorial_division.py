def factorial_division(num1, num2):
    sum1 = 1
    sum2 = 1
    for number1 in range(1, num1 + 1):
        sum1 *= number1
    for number2 in range(1, num2 + 1):
        sum2 *= number2

    result = sum1 / sum2

    return f"{result:.2f}"


integer1 = int(input())
integer2 = int(input())

print(factorial_division(integer1, integer2))
