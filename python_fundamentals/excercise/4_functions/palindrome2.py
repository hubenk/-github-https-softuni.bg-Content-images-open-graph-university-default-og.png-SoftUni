positive_integers = input().split(", ")

for positive_int in positive_integers:
    if int(positive_int) < 10:
        print("True")
    else:
        for x in range(len(positive_int) // 2):
            if positive_int[int(x)] != positive_int[int(x) - 1]:
                print("False")
                break
            print("True")
