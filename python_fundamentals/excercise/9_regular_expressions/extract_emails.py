import re

random_strings = input()

regex = r"(?<=\s)([a-z0-9]+[\-\.\_a-z0-9]*)@[a-z\-]+(\.[a-z]+)+\b"

emails = re.finditer(regex, random_strings)

for mail in emails:
    print(mail.group())
