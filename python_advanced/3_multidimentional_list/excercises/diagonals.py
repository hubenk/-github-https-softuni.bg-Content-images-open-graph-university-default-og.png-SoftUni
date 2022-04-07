rows_number = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []
y = rows_number - 1
for _ in range(rows_number):
    matrix.append([int(x) for x in input().split(", ")])

for x in range(rows_number):
    primary_diagonal.append(matrix[x][x])
    secondary_diagonal.append(matrix[x][y])
    y -= 1

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
