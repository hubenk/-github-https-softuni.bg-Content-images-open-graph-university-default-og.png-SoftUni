initial_string = input()


new_password = ""
command = input()

while command != "Done":
    action = command.split()
    temp_index = 0

    if action[0] == "TakeOdd":
        for char in initial_string:
            if temp_index % 2 != 0:
                new_password += char
            temp_index += 1
        print(new_password)

    elif action[0] == "Cut":
        index = int(action[1])
        length = int(action[2])
        end = index + length
        new_password = new_password[:index] + new_password[end:]
        print(new_password)

    elif action[0] == "Substitute":
        substring = action[1]
        substitute = action[2]

        if substring not in new_password:
            print("Nothing to replace!")
        else:
            new_password = new_password.replace(substring, substitute)
            print(new_password)

    command = input()

print(f"Your password is: {new_password}")