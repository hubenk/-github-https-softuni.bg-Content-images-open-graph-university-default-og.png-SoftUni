key = int(input())
loops = int(input())
message = ""

for x in range(loops):
    letter = input()
    message = (ord(letter) + key)
    print(chr(message), end="")
    