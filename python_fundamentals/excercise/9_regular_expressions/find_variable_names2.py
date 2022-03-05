import re

names = input()
output = []
regex = r"\b_([a-zA-Z0-9]+)\b"
result = re.findall(regex, names)

print(",".join(result))
