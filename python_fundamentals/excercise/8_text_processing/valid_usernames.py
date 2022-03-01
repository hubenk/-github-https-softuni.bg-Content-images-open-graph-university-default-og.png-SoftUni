usernames = input().split(", ")

for name in usernames:
    validation = True
    if 2 < len(name) < 17:
        for char in name:
            if not char.isalnum():
                validation = False
                if char == "-" or char == "_":
                    validation = True

        if validation:
            print(name)
