words = input().split(" ")
occurrences = {}

for word in words:
    for char in word:
        if char not in occurrences:
            occurrences[char] = 0
        occurrences[char] += 1

for key, value in occurrences.items():
    print(f"{key} -> {value}")