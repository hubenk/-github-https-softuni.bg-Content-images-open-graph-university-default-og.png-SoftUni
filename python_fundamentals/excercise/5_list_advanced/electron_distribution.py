electrons = int(input())
shells = 0
result = []

while electrons > 0:
    shells += 1
    max_electrons = 2 * shells ** 2

    if electrons >= max_electrons:
        electrons -= max_electrons
        result.append(max_electrons)
    else:
        result.append(electrons)
        break

print(result)
