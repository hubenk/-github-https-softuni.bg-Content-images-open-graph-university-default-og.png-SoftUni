rows, columns = [int(x) for x in input().split()]
matrix = []
sub_matrix = []
max_sum = -99999
temp_sum = 0
max_start = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for x in range(rows - 2):
    for y in range(columns - 2):
        sub_matrix = []
        temp_sum = 0

        for sub_x in range(x, x + 3):
            temp_matrix = []

            for sub_y in range(y, y + 3):
                temp_matrix.append(matrix[sub_x][sub_y])
            sub_matrix.append(temp_matrix)
            temp_sum += sum(temp_matrix)

        if temp_sum > max_sum:
            max_sum = temp_sum
            max_start.clear()
            max_start.append(x)
            max_start.append(y)

print(f"Sum = {max_sum}")
for row in range(max_start[0], max_start[0] + 3):
    for col in range(max_start[1], max_start[1] + 3):
        print(matrix[row][col], end=" ")
    print()