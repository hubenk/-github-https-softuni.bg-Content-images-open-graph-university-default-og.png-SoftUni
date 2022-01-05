number = int(input())

if number == 3 or number == 5 or number == 7:
    print("True")
elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
    print("False")
else:
    print("True")
