start = int(input())
end = int(input())
magic_number = int(input())
count = 0
number_x = 0
number_y = 0
found_magic_number = False

for x in range(start, end + 1):
    number_x = x
    for y in range(start, end + 1):
        number_y = y
        count += 1
        if number_y + number_x == magic_number:
            found_magic_number = True
            break
    if found_magic_number:
        break

if found_magic_number:
    print(f"Combination N:{count} ({number_x} + {number_y} = {magic_number})")

else:
    print(f"{count} combinations - neither equals {magic_number}")