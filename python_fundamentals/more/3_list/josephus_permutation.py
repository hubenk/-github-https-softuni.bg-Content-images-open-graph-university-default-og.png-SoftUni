people = input().split()
execution = int(input())
dead = list()
counter = 0
temp_list = list()

while len(people) > 0:

    temp_list.clear()

    for execute in people:
        counter += 1
        if counter % execution == 0:
            temp_list.append(execute)
            dead.append(int(execute))

    for remove in temp_list:
        people.remove(remove)

print(str(dead).replace(" ", ""))
