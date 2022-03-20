import re

places = input()
regex = r"(\=|\/)([A-Z][A-Za-z]{2,})(\1)"
travel_points = 0
final_places = list()

valid_places = re.finditer(regex, places)
for valid in valid_places:
    clear_place = valid.group()
    final_places.append(clear_place[1:-1])
    travel_points += len(clear_place) - 2

print(f"Destinations: {(', '.join(final_places))}")
print(f"Travel Points: {travel_points}")