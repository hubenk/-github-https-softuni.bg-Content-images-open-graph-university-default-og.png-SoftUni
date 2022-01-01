letters = input()
upper_letters = []

for x in range(len(letters)):
    if letters[x].isupper():
        upper_letters.append(x)

print(upper_letters)
