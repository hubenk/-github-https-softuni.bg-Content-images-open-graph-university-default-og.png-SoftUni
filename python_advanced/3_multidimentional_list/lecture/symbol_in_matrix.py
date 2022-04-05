row_col = int(input())
matrix = []
symbol_row = 0
symbol_col = 0
found_symbol = False

for _ in range(row_col):
    matrix.append([x for x in input()])

searching_symbol = input()

for x in range(row_col):
    if not found_symbol:
        for y in range(row_col):
            if matrix[x][y] == searching_symbol:
                symbol_row = x
                symbol_col = y
                found_symbol = True
                break

if found_symbol:
    print(f"({symbol_row}, {symbol_col})")
else:
    print(f"{searching_symbol} does not occur in the matrix")
