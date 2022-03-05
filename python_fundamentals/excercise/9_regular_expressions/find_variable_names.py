import re

names = input()
output = []
regex = r"\b(_)([a-z]|[A-Z]|[\d])+\b"
under_regex = r"\b([a-z]|[A-Z]|[\d])+\b"

match = re.finditer(regex, names)
for el in match:
    final_string = el.group()
    result = ""
    for char in final_string:
        if char != "_":
            result += char
    output.append(result)
print(",".join(output))
