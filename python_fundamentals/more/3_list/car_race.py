from math import floor

times = input().split()
left_time = 0
right_time = 0
finish = floor(len(times) / 2)

for first_time in times[:finish]:
    left_time += int(first_time)
    if int(first_time) == 0:
        left_time *= 0.8

for second_time in times[len(times): finish: -1]:
    right_time += int(second_time)
    if int(second_time) == 0:
        right_time *= 0.8

if left_time > right_time:
    print(f"The winner is right with total time: {right_time:.1f}")
else:
    print(f"The winner is left with total time: {left_time:.1f}")
