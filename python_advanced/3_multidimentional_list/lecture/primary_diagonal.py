cube_size = int(input())
matrix = []
sum_diagonal = 0

for _ in range(cube_size):
    matrix.append([int(x) for x in input().split()])

for row_col in range(cube_size):
    sum_diagonal += matrix[row_col][row_col]

print(sum_diagonal)
