characters = input().split(", ")
ascii_dict = {}

for symbol in characters:
    ascii_dict[symbol] = ord(symbol)

print(ascii_dict)