n1 = int(input())
n2 = int(input())
operator = input()
sum = 0

if n2 == 0:
    print(f"Cannot divide {n1} by zero")

elif operator == "+":
    sum = n1 + n2
    if sum % 2 == 0:
        print(f"{n1} {operator} {n2} = {sum} - even")
    else:
        print(f"{n1} {operator} {n2} = {sum} - odd")

elif operator == "-":
    sum = n1 - n2
    if sum % 2 == 0:
        print(f"{n1} {operator} {n2} = {sum} - even")
    else:
        print(f"{n1} {operator} {n2} = {sum} - odd")

elif operator == "*":
    sum = n1 * n2
    if sum % 2 == 0:
        print(f"{n1} {operator} {n2} = {sum} - even")
    else:
        print(f"{n1} {operator} {n2} = {sum} - odd")

elif operator == "/":
    sum = n1 / n2
    print(f"{n1} / {n2} = {sum:.2f}")

elif operator == "%":
    sum = n1 % n2
    print(f"{n1} % {n2} = {sum}")




