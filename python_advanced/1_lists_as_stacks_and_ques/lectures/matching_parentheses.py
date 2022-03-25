algebraic_expression = [x for x in input()]
start_index = []
end_index = []
index_count = 0

for el in algebraic_expression:
    if el == "(":
        start_index.append(index_count)
    if el == ")":
        end_index.append(index_count)
        for x in range(start_index.pop(), end_index.pop() + 1):
            print(algebraic_expression[x], end="")
        print()
    index_count += 1