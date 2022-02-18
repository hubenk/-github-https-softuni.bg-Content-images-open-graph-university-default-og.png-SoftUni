import re

phone_numbers = input()

regex = r"\+359([\s-])2(\1)\d{3}(\1)\d{4}\b"

matched = re.finditer(regex, phone_numbers)
result = [match.group() for match in matched]

print(", ".join(result))
