import re

string_input = input()
loop_check = string_input

while loop_check != "":

    regex = r"\d+"
    match_numbers = re.finditer(regex, string_input)
    for match in match_numbers:
        print(match.group(), end=" ")

    string_input = input()
    loop_check = string_input

# string_input = input()
# while True:
#     if string_input:
#         print()
#         string_input = input()
#     else:
#         break
