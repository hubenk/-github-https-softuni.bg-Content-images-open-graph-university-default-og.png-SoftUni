def squares(n):
    for x in range(1, n + 1):
        result = x * x
        yield result

print(list(squares(5)))