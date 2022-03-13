targets = [int(aim) for aim in input().split()]
index = input()
shot_indexes = []
temp_number = 0

while index != "End":
    index = int(index)
    if index in shot_indexes or len(targets) <= index:
        index = input()
        continue

    shot_indexes.append(index)
    temp_number = targets[index]
    targets[index] = -1

    for index, number in enumerate(targets):
        if number == -1:
            pass
        else:
            if number > temp_number:
                targets[index] -= temp_number
            else:
                targets[index] += temp_number

    index = input()

targets = [str(aim) for aim in targets]
targets = " ".join(targets)
print(f"Shot targets: {len(shot_indexes)} -> {targets}")
