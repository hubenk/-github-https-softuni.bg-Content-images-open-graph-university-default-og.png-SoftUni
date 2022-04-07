rows_number = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []
y = rows_number - 1

for _ in range(rows_number):
    matrix.append([int(x) for x in input().split()])

for x in range(rows_number):
    primary_diagonal.append(matrix[x][x])
    secondary_diagonal.append(matrix[x][y])
    y -= 1

result = sum(primary_diagonal) - sum(secondary_diagonal)
print(abs(result))
