symbols = input().split(" ")
odd_word = {}

for index in symbols:
    word = index.lower()
    if word not in odd_word:
        odd_word[word] = 0
    odd_word[word] += 1

for key, value in odd_word.items():
    if value % 2 != 0:
        print(key, end=" ")
