strings = [x.upper() for x in input()]
rage_output = ""
temp_string = ""

for index in range(len(strings)):
    if strings[index].isdigit() is False:
        temp_string += strings[index]
    else:
        number = int(strings[index])
        rage_output += (temp_string * number)
        temp_string = ""

unique_symbols = [x for x in strings if x.isdigit() is False]
print(f"Unique symbols used: {len(set(unique_symbols))}")
print(rage_output)
