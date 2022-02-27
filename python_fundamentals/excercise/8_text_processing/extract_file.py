path = input()
substracted = ""
path = path[::-1]

for char in path:
    if char == "\\":
        break
    else:
        substracted += char

substracted = substracted[::-1]
name, extension = substracted.split(".")

print(f"File name: {name}")
print(f"File extension: {extension}")