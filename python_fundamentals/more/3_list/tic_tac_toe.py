count = 0
first_player = 0
second_player = 0

while count < 3:
    moves = input().split()
    count += 1

    for x in moves:
        if x == 0:
            pass
        elif x == "1":
            first_player += 1
        elif x == "2":
            second_player += 1

if first_player > second_player:
    print("First player won")
elif first_player < second_player:
    print("Second player won")
else:
    print("Draw!")
