rows, columns = [int(x) for x in input().split(", ")]
matrix = []
sum_submatrix = -9999999
top_row = 0
top_col = 0
bot_row = 0
bot_col = 0

for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

for row in range(rows - 1):
    for col in range(columns - 1):
        temp_square = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if temp_square > sum_submatrix:
            sum_submatrix = temp_square
            top_row, top_col, bot_row, bot_col = matrix[row][col], matrix[row][col+1], matrix[row+1][col], matrix[row+1][col+1]

print(f"{top_row} {top_col}")
print(f"{bot_row} {bot_col}")
print(sum_submatrix)
