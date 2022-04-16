def operate(operator, *args):

    if operator in ("+", "-"):
        result = 0
    else:
        result = 1

    if operator == "+":
        for x in args:
            result += x

    elif operator == "-":
        for x in args:
            result -= x

    elif operator == "*":
        for x in args:
            result *= x

    elif operator == "/":
        for x in args:
            result /= x

    return result


print(operate("-", 1, 2, 3))
print(operate("/", 3, 4))
