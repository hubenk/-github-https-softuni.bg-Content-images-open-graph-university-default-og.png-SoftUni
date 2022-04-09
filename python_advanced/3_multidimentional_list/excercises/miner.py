field_size = int(input())
commands = input().split()
field_matrix = []
start_index = []
coals = 0
collected_coals = False
game_over = False

for x in range(field_size):
    temp_row = input().split()
    field_matrix.append(temp_row)
    if "s" in temp_row:
        start_index.append(x)
        start_index.append(temp_row.index("s"))

    for coal in temp_row:
        if coal == "c":
            coals += 1

while commands:
    move = commands.pop(0)

    if move == "left":
        start_index[1] -= 1
        if start_index[1] < 0:
            start_index[1] += 1

    elif move == "right":
        start_index[1] += 1
        if start_index[1] >= field_size:
            start_index[1] = field_size - 1

    elif move == "down":
        start_index[0] += 1
        if start_index[0] >= field_size:
            start_index[0] = field_size - 1

    elif move == "up":
        start_index[0] -= 1
        if start_index[0] < 0:
            start_index[0] = 0

    if field_matrix[start_index[0]][start_index[1]] == "c":
        field_matrix[start_index[0]][start_index[1]] = "*"
        coals -= 1
        if coals == 0:
            collected_coals = True
            break
    elif field_matrix[start_index[0]][start_index[1]] == "e":
        game_over = True
        break


if collected_coals:
    print(f"You collected all coal! ({start_index[0]}, {start_index[1]})")
elif game_over:
    print(f"Game over! ({start_index[0]}, {start_index[1]})")
else:
    print(f"{coals} pieces of coal left. ({start_index[0]}, {start_index[1]})")