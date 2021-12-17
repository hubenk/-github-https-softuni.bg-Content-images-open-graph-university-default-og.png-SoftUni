number1 = int(input())
number2 = int(input())
magic_number = int(input())
count = 0
is_magic_number = False

for x in range(number1, number2 + 1):
    for y in range(number1, number2 + 1):
        count += 1
        if x + y == magic_number:
            is_magic_number = True
            print(f"Combination N:{count} ({x} + {y} = {magic_number})")
            break

    if is_magic_number:
        break

if not is_magic_number:
    print(f"{count} combinations - neither equals {magic_number}")


