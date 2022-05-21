import os
from os import path

command = input().split("-")

while not command[0] == "End":
    action = command[0]
    file_name = command[1]

    if action == "Create":
        with open(file_name, "w") as file:
            pass

    elif action == "Add":
        with open(file_name, "a") as file:
            file.writelines(f"{command[2]}\n")

    elif action == "Replace":
        if path.exists(file_name):
            with open(file_name, "r") as file:
                data = file.read()
                data = data.replace(command[2], command[3])
            with open(file_name, "w") as file:
                file.write(data)
        else:
            print("An error occurred")

    elif action == "Delete":
        if path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")

    command = input().split("-")