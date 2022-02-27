path = input().split("\\")

substract = path[-1]

name, extension = substract.split(".")

print(f"File name: {name}")
print(f"File extension: {extension}")