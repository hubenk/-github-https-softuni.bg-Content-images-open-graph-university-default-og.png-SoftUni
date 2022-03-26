lines = int(input())
stack = []

for _ in range(lines):
    queries = [int(x) for x in input().split()]

    if queries[0] == 1:
        stack.append(queries[1])
        min_num = min(stack)
    elif queries[0] == 2 and stack:
        stack.pop(0)

    elif queries[0] == 3 and stack:
        print(max(stack))

    elif queries[0] == 4 and stack:
        print(min(stack))

stack = [str(x) for x in stack]
print(', '.join(stack[::-1]))