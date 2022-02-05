cmnd = input()
force_book = {}

while cmnd != "Lumpawaroo":

    if "|" in cmnd:
        command = cmnd.split(" | ")
        side = command[0]
        user = command[1]

        if side not in force_book:
            force_book[side] = [user]
        else:
            no_value = True
            for key, value in force_book.items():
                if user in value:
                    no_value = False
            if no_value:
                force_book[side].append(user)


    else:
        command = cmnd.split(" -> ")
        user = command[0]
        side = command[1]

        if side not in force_book:
            force_book[side] = [user]
        else:
            force_book[side].append(user)
            for key, value in force_book.items():
                if user in value and key != side:
                    force_book[key].remove(user)

        print(f"{user} joins the {side} side!")

    cmnd = input()

for side in force_book.keys():
    if len(force_book[side]) > 0:
        print(f"Side: {side}, Members: {len(force_book[side])}")

        for value in force_book[side]:
            print(f"! {value}")