number_of_letters = int(input())

for x in range(97, 97 + number_of_letters):
    for y in range(97, 97 + number_of_letters):
        for z in range(97, 97 + number_of_letters):
            print(chr(x)+chr(y)+chr(z))
