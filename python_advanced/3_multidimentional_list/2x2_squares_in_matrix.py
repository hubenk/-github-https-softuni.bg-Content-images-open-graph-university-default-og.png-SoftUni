rows, columns = [int(x) for x in input().split()]
matrix = []
identical_submatrix = 0

for _ in range(rows):
    matrix.append([x for x in input().split()])

for row in range(rows - 1):
    for col in range(columns - 1):
        temp_square = matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]
        if len(set(temp_square)) == 1:
            identical_submatrix += 1

print(identical_submatrix)
