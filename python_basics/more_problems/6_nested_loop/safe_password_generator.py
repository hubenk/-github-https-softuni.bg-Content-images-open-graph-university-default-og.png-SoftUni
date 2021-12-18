a = int(input())
b = int(input())
max_number_password = int(input())
counter = 0
enough_passwords = False

for a1 in range(35, 55 + 1):
    if enough_passwords:
        break

    for b1 in range(64, 96 + 1):
        if enough_passwords:
            break

        for x in range(1, a + 1):
            if enough_passwords:
                break

            for y in range(1, b + 1):

                print(f"{chr(a1)}{chr(b1)}{x}{y}{chr(b1)}{chr(a1)}", end="|")
                counter += 1
                if y == b and x == a:
                    enough_passwords = True
                elif counter == max_number_password:
                    enough_passwords = True
                    if enough_passwords:
                        break

                a1 += 1
                if a1 > 55:
                    a1 = 35
                b1 += 1
                if b1 > 96:
                    b1 = 64
