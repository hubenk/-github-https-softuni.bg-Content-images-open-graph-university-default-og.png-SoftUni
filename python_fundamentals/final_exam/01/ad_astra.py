import re
from math import floor

text_string = input()
regex = r"(\#|\|)([A-Za-z\s]+)(\1)([0-9]{2}/[0-9]{2}/[0-9]{2})(\1)([1-9][0-9]+)(\1)"
total_calories = 0
item = ""
date = ""
calories = ""
final_list = []

match_regex = re.finditer(regex, text_string)

for result in match_regex:

    if "#" in result.group():
        clear_result = result.group().split("#")[1:-1]
        item, date, calories = clear_result

    elif "|" in result.group():
        clear_result = result.group().split("|")[1:-1]
        item, date, calories = clear_result

    total_calories += int(calories)
    final_list.append([item, date, calories])

food_left = floor(total_calories / 2000)
print(f"You have food to last you for: {food_left} days!")

for item in final_list:
    print(f"Item: {item[0]}, Best before: {item[1]}, Nutrition: {item[2]}")
