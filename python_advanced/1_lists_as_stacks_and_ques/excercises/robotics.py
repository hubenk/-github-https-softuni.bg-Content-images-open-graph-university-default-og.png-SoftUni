from collections import deque

robots = [x for x in input().split(";")]

h, m, s = [int(x) for x in input().split(":")]

product_line = deque()
working_robots = deque()
back_up_dict = {}
index = 0
product = input()
robot = ""
step = 0

while not product == "End":
    product_line.append(product)
    product = input()

while True:
    s += 1
    if s == 60:
        s = 0
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h == 24:
                h = 0

    if not len(robots) == len(working_robots):
        robot, time = robots[index].split("-")
        working_robots.append([robot, int(time)])
        back_up_dict[robot] = int(time)
        index += 1
        print(f"{robot} - {product_line.popleft()} [{h:02d}:{m:02d}:{s:02d}]")

    else:
        if working_robots[0][1] <= 0:
            robot = working_robots[0][0]
            working_robots[0][1] = back_up_dict[working_robots[0][0]]
            print(f"{robot} - {product_line.popleft()} [{h:02d}:{m:02d}:{s:02d}]")
            working_robots.rotate(1)
        else:
            product_line.rotate(-1)

    for x in working_robots:
        x[1] -= 1
        if x[1] == 0:
            step = working_robots.index(x)
            break
    working_robots.rotate(-step)
    step = 0

    if len(product_line) == 0:
        break
