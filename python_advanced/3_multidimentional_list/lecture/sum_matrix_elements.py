rows, columns = [int(x) for x in input().split(", ")]
total_sum = 0
matrix = []

for row in range(rows):
    column = [int(x) for x in input().split(", ")]
    total_sum += sum(column)
    matrix.append(column)

print(total_sum)
print(matrix)
