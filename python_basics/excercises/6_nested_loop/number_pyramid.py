number = int(input())
count = 1
is_number = False

for x in range(1, number + 1):
    for y in range(1,x + 1):
        print(count, end = " ")
        count += 1
        if count > number:
            is_number = True
            break
    print()

    if is_number:
        break
