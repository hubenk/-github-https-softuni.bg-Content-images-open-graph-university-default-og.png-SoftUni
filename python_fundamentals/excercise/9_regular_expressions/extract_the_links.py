import re

mixed_text = input()

regex = r"\b(www.)([a-zA-Z\d\-]+)\.([\.a-z]+)\b"

while mixed_text:

    result = re.finditer(regex, mixed_text)
    for web in result:
        print(web.group())

    mixed_text = input()