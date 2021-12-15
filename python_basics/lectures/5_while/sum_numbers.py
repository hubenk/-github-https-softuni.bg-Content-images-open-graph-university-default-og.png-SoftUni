number = int(input())
sum = 0

while True:                 #while sum < number:
    x = int(input())            #x = int(input)
                                #sum += x
    if sum < number:
        sum += x             #print(sum)
        if sum >= number:
            break

print(sum)