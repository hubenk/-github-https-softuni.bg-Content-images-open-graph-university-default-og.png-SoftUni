loops = int(input())
word = input()
main_strings = []
word_strings = []

for _ in range(loops):
    strings = input()
    main_strings.append(strings)
    if word in strings:
        word_strings.append(strings)

print(main_strings)
print(word_strings)
