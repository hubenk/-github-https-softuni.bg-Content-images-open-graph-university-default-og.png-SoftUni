string_line = input()
digit_list = [int(number) for number in string_line if number.isdigit()]
character_list = [char for char in string_line if not char.isdigit()]

take_list = [number for index, number in enumerate(digit_list) if index % 2 == 0]
skip_list = [number for index, number in enumerate(digit_list) if index % 2 != 0]

take = 0
skip = 0
final_string = ""
temp_index = 0

for _ in range(len(take_list)):
    for char in range(take_list[take]):
        if temp_index == len(character_list):
            break
        else:
            final_string += character_list[temp_index]
            temp_index += 1
    temp_index += skip_list[skip]
    take += 1
    skip += 1

print(final_string)
