import re

participans = input().split(", ")
some_text = input()
score_table = {}
name_regex = r"[A-Za-z+]"
km_regex = r"\d"

while some_text != "end of race":
    temp_name = ""
    temp_km = 0

    name_result = re.finditer(name_regex, some_text)
    for name in name_result:
        temp_name += name.group()

    number_result = re.finditer(km_regex, some_text)
    for km in number_result:
        temp_km += int(km.group())

    if temp_name in participans:
        if temp_name not in score_table:
            score_table[temp_name] = temp_km
        else:
            score_table[temp_name] += temp_km

    some_text = input()

sorted_result = sorted(score_table.items(), reverse=True, key=lambda x: x[1])

print(f"1st place: {sorted_result[0][0]}")
print(f"2nd place: {sorted_result[1][0]}")
print(f"3rd place: {sorted_result[2][0]}")
