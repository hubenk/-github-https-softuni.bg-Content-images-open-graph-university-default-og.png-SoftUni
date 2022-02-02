winner = ""
rows = []

for x in range(3):
    line = input().split(" ")
    rows.append(line)

for player in range(1, 3):
    player = str(player)

    if player == rows[0][0] and player == rows[0][1] and player == rows[0][2]:
        winner = player
        break
    elif player == rows[1][0] and player == rows[1][1] and player == rows[1][2]:
        winner = player
        break
    elif player == rows[2][0] and player == rows[2][1] and player == rows[2][2]:
        winner = player
        break
    elif player == rows[0][0] and player == rows[1][0] and player == rows[2][0]:
        winner = player
        break
    elif player == rows[0][1] and player == rows[1][1] and player == rows[2][1]:
        winner = player
        break
    elif player == rows[0][2] and player == rows[1][2] and player == rows[2][2]:
        winner = player
        break
    elif player == rows[0][0] and player == rows[1][1] and player == rows[2][2]:
        winner = player
        break
    elif player == rows[0][2] and player == rows[1][1] and player == rows[2][0]:
        winner = player
        break

if winner == "1":
    print("First player won")
elif winner == "2":
    print("Second player won")
else:
    print("Draw!")

