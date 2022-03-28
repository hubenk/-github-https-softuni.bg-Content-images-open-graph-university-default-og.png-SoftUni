numbers = [float(x) for x in input().split()]
occurences = {}

for num in numbers:
    if num not in occurences:
        occurences[num] = 1
    else:
        occurences[num] += 1

for key, value in occurences.items():
    print(f"{key:.1f} - {value} times")
