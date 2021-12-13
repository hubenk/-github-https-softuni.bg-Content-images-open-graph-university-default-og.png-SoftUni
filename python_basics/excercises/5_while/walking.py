goal = 10000
actual = 0

while actual < goal:
    steps = input()


    if steps == str("Going home"):
        steps = int(input())
        actual += int(steps)

        if actual < goal:
            diff = goal - actual
            print(f"{diff} more steps to reach goal.")
            break
        elif actual > goal:
            diff = actual - goal
            print("Goal reached! Good job!")
            print(f"{diff} steps over the goal!")
            break

    actual += int(steps)

    if actual >= goal:
        diff = actual - goal
        print("Goal reached! Good job!")
        print(f"{diff} steps over the goal!")
