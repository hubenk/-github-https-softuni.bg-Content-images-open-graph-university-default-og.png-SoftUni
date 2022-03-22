concealed_message = input()
command = input()

while command != "Reveal":
    instructions = command.split(":|:")

    if instructions[0] == "InsertSpace":
        index = int(instructions[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)

    elif instructions[0] == "Reverse":
        substring = instructions[1]

        if substring in concealed_message:
            reversed_string = substring[::-1]
            concealed_message = concealed_message.replace(substring, "", 1)
            concealed_message += reversed_string
            print(concealed_message)
        else:
            print("error")

    elif instructions[0] == "ChangeAll":
        old, new = instructions[1], instructions[2]
        if old in concealed_message:
            concealed_message = concealed_message.replace(old, new)
            print(concealed_message)

    command = input()

print(f"You have a new text message: {concealed_message}")