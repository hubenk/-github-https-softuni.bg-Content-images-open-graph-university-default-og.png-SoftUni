wagons = int(input())
train = [0] * wagons
command = input()

while command != "End":

    comand = command.split()
    if comand[0] == "add":
        train[-1] += int(comand[-1])
    elif comand[0] == "insert":
        index = int(comand[1])
        train[index] += int(comand[-1])
    elif comand[0] == "leave":
        index = int(comand[1])
        train[index] -= int(comand[-1])

    command = input()

print(train)
