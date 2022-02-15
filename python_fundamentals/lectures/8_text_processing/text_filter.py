banned_word = input().split(", ")
checked_text = input()

for word in banned_word:
    temp_word = "*" * len(word)
    while word in checked_text:
        checked_text = checked_text.replace(word, temp_word)

print(checked_text)