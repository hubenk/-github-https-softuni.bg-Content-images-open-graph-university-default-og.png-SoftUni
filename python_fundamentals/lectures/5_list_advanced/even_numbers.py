single_string = input().split(", ")

print([index for index, number in enumerate(single_string) if int(number) % 2 == 0])

