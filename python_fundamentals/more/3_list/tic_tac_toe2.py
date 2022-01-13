first_player = 0
second_player = 0


for x in range(3):
    line = input().split()
    for move in line:
        if move == 0:
            pass
        elif move == "1":
            first_player += 1
        elif move == "2":
            second_player += 1

if first_player > second_player:
    print("First player won")
elif first_player < second_player:
    print("Second player won")
else:
    print("Draw!")
