to_be_replaced = input()
replaced_string = ""
last_letter = ""

for letter in to_be_replaced:
    if letter != last_letter:
        replaced_string += letter
    last_letter = letter

print(replaced_string)