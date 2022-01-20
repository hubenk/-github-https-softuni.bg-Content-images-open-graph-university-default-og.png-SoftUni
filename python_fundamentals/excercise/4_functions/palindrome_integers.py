def polindrome(number):
    for positive_int in number:
        if int(positive_int) < 10:
            print("False")
        else:
            for x in range(len(positive_int)//2):
                if positive_int[int(x)] != positive_int[int(x)-1]:
                    print("False")
                    break
                print("True")



positive_integers = input().split(", ")

print(polindrome(positive_integers))
