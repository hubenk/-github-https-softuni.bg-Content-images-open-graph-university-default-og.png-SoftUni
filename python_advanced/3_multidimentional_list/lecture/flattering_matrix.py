matrix_number = int(input())
matrix = []

for _ in range(matrix_number):
    matrix.extend(int(x) for x in input().split(", "))

print(matrix)