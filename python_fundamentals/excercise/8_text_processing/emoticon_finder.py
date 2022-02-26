emoticon_string = input()
emoticon = ""

for char in emoticon_string:
    if emoticon != "":
        emoticon += char
        print(emoticon)
        emoticon = ""

    if char == ":":
        emoticon += ":"


