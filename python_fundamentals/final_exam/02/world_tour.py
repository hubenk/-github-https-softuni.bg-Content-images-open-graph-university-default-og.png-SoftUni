stops = [x for x in input()]

command = input()

while command != "Travel":
    cmnd1, cmnd2, cmnd3 = command.split(":")

    if cmnd1 == "Add Stop":
        if int(cmnd2) <= len(stops):
            cmnd3 = [x for x in cmnd3]
            for x in cmnd3[::-1]:
                stops.insert(int(cmnd2), x)
        print("".join(stops))


    elif cmnd1 == "Remove Stop":
        if int(cmnd3) < len(stops):
            sliced_list = []
            for x in stops[:int(cmnd2)]:
                sliced_list.append(x)
            for y in stops[int(cmnd3) + 1:]:
                sliced_list.append(y)
            stops = sliced_list
        print("".join(stops))


    elif cmnd1 == "Switch":
        temp_stop = "".join(stops)
        if cmnd2 in temp_stop:
            str1 = [x for x in cmnd2]
            temp_index = stops.index(str1[0])
            for x in range(len(str1)):
                stops.pop(temp_index)
            str2 = [y for y in cmnd3]
            for y in (str2[::-1]):
                stops.insert(temp_index, y)
        print("".join(stops))


    command = input()

print(f"Ready for world tour! Planned stops: {''.join(stops)}")