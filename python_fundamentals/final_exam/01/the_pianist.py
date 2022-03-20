number_of_pieces = int(input())
all_pieces = {}

for x in range(number_of_pieces):
    piece, composer, key = input().split("|")
    all_pieces[piece] = []
    all_pieces[piece] = [composer, key]

commands = input()

while commands != "Stop":
    command = commands.split("|")

    if command[0] == "Add":
        if command[1] in all_pieces:
            print(f"{command[1]} is already in the collection!")
        else:
            all_pieces[command[1]] = []
            all_pieces[command[1]] = [command[2], command[3]]
            print(f"{command[1]} by {command[2]} in {command[3]} added to the collection!")

    elif command[0] == "Remove":
        if command[1] not in all_pieces:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")
        else:
            del all_pieces[command[1]]
            print(f"Successfully removed {command[1]}!")

    elif command[0] == "ChangeKey":
        if command[1] not in all_pieces:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")
        else:
            x = all_pieces[command[1]]
            all_pieces[command[1]][1] = command[2]

            print(f"Changed the key of {command[1]} to {command[2]}!")

    commands = input()

for key, value in sorted(all_pieces.items(), reverse=False, key=lambda x: x):
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
