pairs = int(input())
value = 0
previous_value = 0
max_diff = 0
diff = 0
total_value = 0

for x in range(pairs):
    pair1 = int(input())
    pair2 = int(input())
    value = pair1 + pair2
    total_value += value
    if x == 0:
        previous_value = value

    if x != 0:
        diff = abs(value - previous_value)
        if diff >= max_diff:
            max_diff = diff
    previous_value = value


if total_value / pairs == value:
    print(f"Yes, value={value}")
else:
    print(f"No, maxdiff={max_diff}")