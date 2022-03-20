message = [el for el in input()]
code = input()

while code != "Decode":
    code_list = code.split("|")

    if code_list[0] == "Move":
        moves = int(code_list[1])
        for x in range(moves):
            to_add = message.pop(0)
            message.append(to_add)

    elif code_list[0] == "Insert":
        message.insert(int(code_list[1]), code_list[2])

    elif code_list[0] == "ChangeAll":
        for x in range(len(message)):
            if message[x] == code_list[1]:
                message[x] = code_list[2]

    code = input()

decrypted_message = "".join(message)
print(f"The decrypted message is: {decrypted_message}")
