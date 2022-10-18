rooms = int(input())
chairs_left = 0
no_print = True
for room in range(1, rooms + 1):
    chairs_visitors = input().split()
    chairs = len(chairs_visitors[0])
    visitors = int(chairs_visitors[1])
    if chairs < visitors:
        chairs_left -= (visitors - chairs)
        no_print = False
        print(f"{visitors - chairs} more chairs needed in room {room}")
    else:
        chairs_left += (chairs - visitors)

if no_print:
    print(f"Game On, {chairs_left} free chairs left")
