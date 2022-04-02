import re
from functools import reduce

emojis_counter = 0
cool_emojis = []
strings = input()

regex_words = r"(\:{2}|\*{2})([A-Z]{1}[a-z]{2,})(\1)"
regex_numbers = r"\d"

found_words = re.finditer(regex_words, strings)
found_numbers = re.findall(regex_numbers, strings)

found_numbers = (int(x) for x in found_numbers)
cool_threshold = reduce(lambda x, y: x * y, found_numbers)

for word in found_words:
    emojis_counter += 1
    temp_sum = 0
    temp_word = word.group()[2:-2]
    for el in temp_word:
        temp_sum += ord(el)

    if temp_sum >= cool_threshold:
        cool_emojis.append(word)


print(f"Cool threshold: {cool_threshold}")
print(f"{emojis_counter} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(emoji.group())
