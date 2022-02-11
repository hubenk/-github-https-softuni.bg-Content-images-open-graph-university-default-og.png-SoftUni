data = input()
dwarfs = {}
sorted_dwarfs = {}
while data != "Once upon a time":
    name, color, physics = data.split(" <:> ")

    if name not in dwarfs:
        dwarfs[name] = [color]
        dwarfs[name].append(int(physics))

    elif name in dwarfs:
        if color in dwarfs[name]:
            if dwarfs[name][color] < int(physics):
                dwarfs[name][color] = int(physics)
        elif color not in dwarfs[name]:
            new_list = list()
            new_list.append(color)
            new_list.append(physics)
            dwarfs[name].append(new_list)

    data = input()

sorted_dwarfs = sorted(dwarfs.items(), key=lambda x: (-x[1][1], x[1][0]), reverse=False)

for dwarf in sorted_dwarfs:
    print(f"({dwarf[1][0]}) {dwarf[0]} <-> {dwarf[1][1]}")