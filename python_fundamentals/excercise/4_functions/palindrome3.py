positive_integers = input().split(", ")

for positive_int in positive_integers:
    if positive_int == positive_int[::-1]:
        print("True")
    else:
        print("False")
