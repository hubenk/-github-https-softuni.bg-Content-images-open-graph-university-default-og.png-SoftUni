number_n = int(input())
total = 0

for n in range(1, number_n + 1):
    num1 = n % 10
    num2 = n //10
    total = num1 + num2
    if total == 5 or total == 7 or total == 11:
        print(f"{n} -> True")
    else:
        print(f"{n} -> False")
