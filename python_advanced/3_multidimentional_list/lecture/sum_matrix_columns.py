rows, columns = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(" ")])

for col in range(columns):
    sum_elements = 0
    for row in range(rows):
        sum_elements += matrix[row][col]
    print(sum_elements)

