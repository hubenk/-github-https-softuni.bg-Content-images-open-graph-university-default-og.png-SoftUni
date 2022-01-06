gifts = input().split()
command = input().split()

while True:
    if "Money" in command:
        break

    elif "OutOfStock" in command:
        for index, gift in enumerate(gifts):
            if gift == command[1]:
                gifts[index] = "None"

    elif "Required" in command:
        gifts_index = int(command[2])
        if 0 <= gifts_index < len(gifts):
            gifts[gifts_index] = command[1]

    elif "JustInCase" in command:
        gifts[-1] = command[1]

    command = input().split()
    continue


for index, gift in enumerate(gifts):
    if gift == "None":
        gifts.remove("None")

print(" ".join(gifts))
