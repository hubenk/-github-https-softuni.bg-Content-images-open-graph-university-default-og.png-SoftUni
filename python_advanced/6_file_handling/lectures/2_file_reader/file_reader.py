result = 0

with open("numbers.txt") as file:
    for num in file:
        result += int(num)

print(result)
