dangerious_string = [x for x in input()]
charged_explosions = 0
new_string = ""

for index in range(len(dangerious_string)):

    if dangerious_string[index] != ">":
        if charged_explosions > 0:
            charged_explosions -= 1
        else:
            new_string += dangerious_string[index]

    elif dangerious_string[index] == ">":
        new_string += dangerious_string[index]
        charged_explosions += int(dangerious_string[index + 1])

print(new_string)
