single_string = input()
digits = ""
letters = ""
others = ""

for char in single_string:
    if char.isalpha():
        letters += char
    elif char.isdigit():
        digits += char
    else:
        others += char

print(digits)
print(letters)
print(others)
