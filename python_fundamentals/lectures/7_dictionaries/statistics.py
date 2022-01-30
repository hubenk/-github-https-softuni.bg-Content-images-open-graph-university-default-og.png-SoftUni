command = input()
dictionary = {}

while command != "statistics":
    data = command.split(": ")
    key = data[0]
    value = data[1]

    if key not in dictionary:
        dictionary[key] = int(value)
    else:
        dictionary[key] += int(value)

    command = input()


print("Products in stock:")

for key, value in dictionary.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(dictionary.keys())}")
print(f"Total Quantity: {sum(dictionary.values())}")