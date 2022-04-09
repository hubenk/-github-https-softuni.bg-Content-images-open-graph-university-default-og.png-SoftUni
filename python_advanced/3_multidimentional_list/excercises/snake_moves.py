from collections import deque
rows, columns = [int(x) for x in input().split()]
matrix = []
snake = []
word = deque(input())

for el in range(rows * columns):
    snake.append(word[0])
    word.rotate(-1)

for row in range(rows):
    temp_row = []
    for col in range(columns):
        temp_el = snake.pop(0)
        temp_row.append(temp_el)
    if row % 2 != 0:
        reverse_row = temp_row[::-1]
        matrix.append(reverse_row)
    else:
        matrix.append(temp_row)

for x in range(rows):
    print("".join(matrix[x]))
