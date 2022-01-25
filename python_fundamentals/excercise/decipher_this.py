secret_message = input().split()
new_sentence = ""

for piece in secret_message:
    digit = ""
    new_word = ""
    first_part = ""
    second_part = []

    for character in piece:

        if character.isdigit():
            digit += character
        else:
            second_part.append(character)

    if len(second_part) > 1:
        second_part[0], second_part[-1] = second_part[-1], second_part[0]

    first_part += chr(int(digit))

    for letter in second_part:
        first_part += letter

    new_sentence += first_part + " "

print(new_sentence)
