width = int(input())
lenght = int(input())
height = int(input())
volume = width * lenght * height

while True:
    command = input()

    if command == "Done":
        print(f"{volume} Cubic meters left.")
        break
    volume -= int(command)

    if volume < 0:
        volume = abs(volume)
        print(f"No more free space! You need {volume} Cubic meters more.")
        break
