string_one = input()
string_two = input()
last_string = string_one
unique_string = ""

for x in range(1, len(string_one) + 1):
    first_part = string_two[:x]
    second_part = string_one[x:]
    unique_string = first_part + second_part
    if unique_string != last_string:
        print(unique_string)
    last_string = unique_string

