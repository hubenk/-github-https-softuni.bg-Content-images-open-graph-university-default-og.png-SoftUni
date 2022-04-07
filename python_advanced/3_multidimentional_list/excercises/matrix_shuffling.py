rows, columns = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append(input().split())

command = input().split()
while not command[0] == "END":
    if not command[0] == "swap":
        print("Invalid input!")
        command = input().split()
        continue
    elif not len(command) == 5:
        print("Invalid input!")
        command = input().split()
        continue
    elif int(command[1]) > rows or int(command[3]) > rows or int(command[2]) > columns or int(command[4]) > columns:
        print("Invalid input!")
        command = input().split()
        continue

    r1, c1, r2, c2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])

    matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]

    for row in range(rows):
        print(*matrix[row])

    command = input().split()
