import re
numbers = input()

regex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

matched_numbers = re.finditer(regex, numbers)

for match in matched_numbers:
    print(match.group(), end=" ")

