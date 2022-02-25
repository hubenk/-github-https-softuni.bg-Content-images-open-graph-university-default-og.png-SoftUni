encrypt_me = input()
encrypted_text = ""

for letter in encrypt_me:
    new_letter = chr(ord(letter)+3)
    encrypted_text += new_letter

print(encrypted_text)
