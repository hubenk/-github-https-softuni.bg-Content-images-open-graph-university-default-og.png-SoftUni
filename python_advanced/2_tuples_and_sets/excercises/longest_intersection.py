ranges = int(input())
longest_intersection = []

for _ in range(ranges):
    range1, range2 = input().split("-")
    start1, end1 = range1.split(",")
    start2, end2 = range2.split(",")
    compare1 = set()
    compare2 = set()

    for x in range(int(start1), int(end1) + 1):
        compare1.add(x)
    for y in range(int(start2), int(end2) + 1):
        compare2.add(y)

    temp_intersection = compare1.intersection(compare2)
    if len(temp_intersection) > len(longest_intersection):
        longest_intersection = temp_intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
