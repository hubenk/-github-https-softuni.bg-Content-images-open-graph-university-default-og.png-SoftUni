rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

command = input().split()
while not command[0] == "END":
    action, row, col, value = command

    if 0 <= int(row) <= rows and 0 <= int(col) < len(matrix):
        if action == "Add":
            matrix[int(row)][int(col)] += int(value)

        elif action == "Subtract":
            matrix[int(row)][int(col)] -= int(value)
    else:
        print("Invalid coordinates")

    command = input().split()

for x in matrix:
    print(*x)