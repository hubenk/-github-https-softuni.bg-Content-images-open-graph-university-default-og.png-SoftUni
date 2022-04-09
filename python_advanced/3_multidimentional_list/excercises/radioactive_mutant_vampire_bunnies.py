rows, columns = [int(x) for x in input().split()]
matrix = []
commands = []
players_index = []
bunny_index = []
next_matrix = []

win = False
dead = False

for row in range(rows):
    temp_row = [x for x in input()]
    matrix.append(temp_row)
    next_row = ["."] * columns
    next_matrix.append(next_row)

    if "P" in temp_row:
        col = temp_row.index("P")
        players_index.append(row)
        players_index.append(col)

commands = [x for x in input()]

while True:
    move = commands.pop(0)

    matrix[players_index[0]][players_index[1]] = "."

    if move == "L":
        players_index[1] -= 1
        if players_index[1] < 0:
            players_index[1] = 0
            win = True
            # break

    elif move == "R":
        players_index[1] += 1
        if players_index[1] == columns:
            players_index[1] = columns -1
            win = True
            # break

    elif move == "U":
        players_index[0] -= 1
        if players_index[0] < 0:
            players_index[0] = 0
            win = True
            # break

    elif move == "D":
        players_index[0] += 1
        if players_index[0] == rows:
            players_index[0] = rows - 1
            win = True
            # break

    if matrix[players_index[0]][players_index[1]] == "B":
        dead = True

    for index, bunny in enumerate(matrix):
        bunny_index.clear()
        for el in bunny:
            if el == "B":
                bunny_index_col = bunny.index("B")
                bunny_index.append(index)
                bunny_index.append(bunny_index_col)
                next_matrix[bunny_index[0]][bunny_index[1]] = "B"

                if bunny_index[0] - 1 >= 0:
                    if matrix[bunny_index[0] - 1][bunny_index[1]] == "P":
                        dead = True
                    next_matrix[bunny_index[0] - 1][bunny_index[1]] = "B"

                if bunny_index[0] + 1 < rows:
                    if matrix[bunny_index[0] + 1][bunny_index[1]] == "P":
                        dead = True
                    next_matrix[bunny_index[0] + 1][bunny_index[1]] = "B"

                if bunny_index[1] - 1 >= 0:
                    if matrix[bunny_index[0]][bunny_index[1] - 1] == "P":
                        dead = True
                    next_matrix[bunny_index[0]][bunny_index[1] - 1] = "B"

                if bunny_index[1] + 1 < columns:
                    if matrix[bunny_index[0]][bunny_index[1] + 1] == "P":
                        dead = True
                    next_matrix[bunny_index[0]][bunny_index[1] + 1] = "B"

    matrix = next_matrix.copy()
    if dead or win:
        break


for r in matrix:
    print("".join(r))

if win:
    print(f"won: {players_index[0]} {players_index[1]}")
else:
    print(f"dead: {players_index[0]} {players_index[1]}")