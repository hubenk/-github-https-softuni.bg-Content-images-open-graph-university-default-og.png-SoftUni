rows, columns = [int(x) for x in input().split()]
final_matrix = []

for row in range(rows):
    row_list = []
    for col in range(columns):
        letter = row + col + 97
        first_last = row + 97
        middle = chr(letter)
        palindrome = chr(first_last) + middle + chr(first_last)
        row_list.append(palindrome)

    final_matrix.append(row_list)

for x in range(len(final_matrix)):
    print(*final_matrix[x])
