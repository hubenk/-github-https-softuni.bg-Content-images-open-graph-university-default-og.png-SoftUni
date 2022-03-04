import re

strings = input()
word = input()
regex = fr"\b{word}\b"
result = re.findall(regex, strings, flags=re.I)

print(len(result))

