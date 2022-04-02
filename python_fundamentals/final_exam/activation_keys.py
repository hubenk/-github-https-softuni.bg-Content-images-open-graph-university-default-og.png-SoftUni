key = input()
command = input().split(">>>")

while not command[0] == "Generate":

    if command[0] == "Contains":
        if not key.find(command[1]) == -1:
            print(f"{key} contains {command[1]}")
        else:
            print("Substring not found!")

    elif command[0] == "Flip":
        start = int(command[2])
        end = int(command[3])
        substring = key[start:end]
        new_substring = ""
        if command[1] == "Upper":
            new_substring = substring.upper()
        elif command[1] == "Lower":
            new_substring = substring.lower()
        key = key[:start] + new_substring + key[end:]
        print(key)

    elif command[0] == "Slice":
        start = int(command[1])
        end = int(command[2])
        new_key = key[:start] + key[end:]
        key = new_key
        print(key)

    command = input().split(">>>")

print(f"Your activation key is: {key}")