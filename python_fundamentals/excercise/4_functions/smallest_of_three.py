def smallest_number(num1, num2, num3):
    list_of_numbers = [num1, num2, num3]
    smallest = min(list_of_numbers)
    return smallest


number1 = int(input())
number2 = int(input())
number3 = int(input())

print(smallest_number(number1, number2, number3))

