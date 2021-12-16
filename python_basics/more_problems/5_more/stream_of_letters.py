word = ""
count_c = 0
count_o = 0
count_n = 0
final_word = ""

while True:
    letter = input()
    if count_o > 0 and count_n > 0 and count_c > 0:
        word += " "
        final_word += word
        word = ""
        count_c = 0
        count_n = 0
        count_o = 0

    if letter == "End":
        print(final_word)
        break

    if letter.isalpha():
        if letter == "c":
            count_c += 1
            if count_c > 1:
                word += letter
        elif letter == "o":
            count_o += 1
            if count_o > 1:
                word += letter
        elif letter == "n":
            count_n += 1
            if count_n > 1:
                word += letter
        else:
            word += letter





