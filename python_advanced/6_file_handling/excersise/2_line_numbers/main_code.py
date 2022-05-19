counter = 1
with open("input_text.txt") as file:
    for line in file:
        letter = 0
        punctuation = 0
        no_space = line.replace(" ", "").strip()
        for el in no_space:
            if el.isalpha():
                letter += 1
            else:
                punctuation += 1

        new_line = f"Line {counter}: {line} ({letter})({punctuation})\n"
        with open("output.txt", "a") as file_line:
            file_line.writelines(new_line)

        counter += 1