queue = int(input())
wagons = [int(unit) for unit in input().split()]
available_space = len(wagons) * 4
max_load = 4
queue += sum(wagons)

for index in range(len(wagons)):
    if max_load > available_space or max_load > queue:
        if available_space > queue:
            max_load = queue
        else:
            max_load = available_space

    queue -= max_load
    wagons[index] = max_load
    available_space -= max_load


if queue > 0 and available_space == 0:
    print(f"There isn't enough space! {queue} people in a queue!")
    print(*wagons)
elif queue == 0 and available_space > 0:
    print("The lift has empty spots!")
    print(*wagons)
elif queue == 0 and available_space == 0:
    print(*wagons)
