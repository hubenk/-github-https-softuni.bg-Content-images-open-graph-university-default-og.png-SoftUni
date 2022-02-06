phone_numbers = input()
phonebook = {}

while phone_numbers.isnumeric() is False:
    name_number = phone_numbers.split("-")

    phonebook[name_number[0]] = name_number[1]

    phone_numbers = input()

search = int(phone_numbers)

for _ in range(search):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")