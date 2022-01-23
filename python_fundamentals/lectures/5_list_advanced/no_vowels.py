text = input()
vowels = ["a", "e", "o", "i", "u"]
list_text = [symbol for symbol in text if symbol not in vowels]

print("".join(list_text))
