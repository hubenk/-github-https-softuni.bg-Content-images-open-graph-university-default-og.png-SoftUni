text = input()
occurrences = {}

for el in text:
    if el not in occurrences:
        occurrences[el] = 1
    else:
        occurrences[el] += 1

for key, value in sorted(occurrences.items()):
    print(f"{key}: {value} time/s")