row_col = int(input())
board = []
removed_horses = 0

for _ in range(row_col):
    board.append([x for x in input()])

while True:
    max_moves_coordinates = []
    max_moves = 0

    for row in range(row_col):
        for col in range(row_col):
            temp_moves = 0
            if board[row][col] == "K":
                if 0 <= row - 2 and 0 <= col - 1:
                    if board[row-2][col-1] == "K":
                        temp_moves += 1
                if 0 <= row - 2 and col + 1 < row_col:
                    if board[row-2][col+1] == "K":
                        temp_moves += 1
                if 0 <= row - 1 and 0 <= col - 2:
                    if board[row-1][col - 2] == "K":
                        temp_moves += 1
                if row + 1 < row_col and 0 <= col - 2:
                    if board[row+1][col-2] == "K":
                        temp_moves += 1
                if row + 2 < row_col and 0 <= col - 1:
                    if board[row+2][col-1] == "K":
                        temp_moves += 1
                if row + 2 < row_col and col + 1 < row_col:
                    if board[row+2][col+1] == "K":
                        temp_moves += 1
                if row + 1 < row_col and 0 <= col - 2:
                    if board[row+1][col-2] == "K":
                        temp_moves += 1
                if 0 <= row - 1 and col + 2 < row_col:
                    if board[row-1][col+2] == "K":
                        temp_moves += 1

            if temp_moves > max_moves:
                max_moves_coordinates.clear()
                max_moves = temp_moves
                max_moves_coordinates.append(row)
                max_moves_coordinates.append(col)

    if max_moves_coordinates:
        board[max_moves_coordinates[0]][max_moves_coordinates[1]] = "0"
        removed_horses += 1
    else:
        break

print(removed_horses)
