start_letter = input()
end_letter = input()
skip_letter = input()
count = 0

for x in range(ord(start_letter), ord(end_letter) + 1):
    for y in range(ord(start_letter), ord(end_letter) + 1):
        for z in range(ord(start_letter), ord(end_letter) + 1):
            if chr(x) != skip_letter and chr(y) != skip_letter and chr(z) != skip_letter:
                count += 1
                print(f"{chr(x)}{chr(y)}{chr(z)}", end=" ")
print(count)

