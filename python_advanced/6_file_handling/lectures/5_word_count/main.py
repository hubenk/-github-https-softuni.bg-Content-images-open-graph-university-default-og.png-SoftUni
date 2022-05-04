import re

with open("words.txt", "r") as file:
    searched_words = file.read().split()

found_words = {}

with open("input.txt", "r") as file:
    text = file.read()
    for word in searched_words:
        regex = fr"\b{word}\b"
        count = len(re.findall(regex, text, re.IGNORECASE))
        found_words[word] = count


with open("output.txt", "w") as file:
    for key, value in sorted(found_words.items(), key=lambda x: -x[1]):
        file.writelines(f"{key} - {value}\n")
