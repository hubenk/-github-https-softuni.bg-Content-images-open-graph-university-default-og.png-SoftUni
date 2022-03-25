from collections import deque

quantity_of_water = int(input())
people = deque()

command = input()

while not command == "Start":
    people.append(command)

    command = input()

command = input()
while not command == "End":

    action = command.split()

    if action[0] == "refill":
        quantity_of_water += int(action[1])

    else:
        if int(action[0]) > quantity_of_water:
            print(f"{people.popleft()} must wait")
        else:
            quantity_of_water -= int(action[0])
            print(f"{people.popleft()} got water")

    command = input()

print(f"{quantity_of_water} liters left")