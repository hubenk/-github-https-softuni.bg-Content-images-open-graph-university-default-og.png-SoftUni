floors = int(input())
rooms = int(input())
room_numbers = ""

for x in range(floors, 0, -1):
    for y in range(0, rooms):
        current_number = x * 10 + y
        if x == floors:
            print(f"L{current_number} ", end = "")

        elif x % 2 == 0:
            room_numbers += f"O{current_number} "

        else:
            room_numbers += f"A{current_number} "

    print(room_numbers)
    room_numbers = ""

