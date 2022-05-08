counter = 0
chars_replace = ["-", ",", ".", "!", "?"]

with open("text.txt", "r") as file:
    for line in file:
        if counter % 2 == 0:
            for char in chars_replace:
                line = line.replace(char, "@")
            print(" ".join(line.split()[::-1]))

        counter += 1
