import re

text = input()
regex = r"(@|#)([A-Za-z]{3,})(\1){2}([A-Za-z]{3,})(\1)"
storage = list()
clear_text = re.finditer(regex, text)
pairs = 0

for word in clear_text:
    clear_word = word.group()
    if "#" in clear_word:
        pairs += 1
        split_words = clear_word.split("#")
        word1 = split_words[1]
        word2 = split_words[3]
        if word1 == word2[::-1]:
            storage.append(f"{word1} <=> {word2}")

    elif "@" in clear_word:
        pairs += 1
        split_words = clear_word.split("@")
        word1 = split_words[1]
        word2 = split_words[3]
        if word1 == word2[::-1]:
            storage.append(f"{word1} <=> {word2}")

if pairs == 0:
    print("No word pairs found!")
else:
    print(f"{pairs} word pairs found!")

if len(storage) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(storage))
