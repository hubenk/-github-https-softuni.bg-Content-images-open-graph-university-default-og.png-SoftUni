initial_array = [int(number) for number in input().split()]
command = input().split()

while command[0] != "end":

    if command[0] == "swap":
        index1 = int(command[1])
        index2 = int(command[2])
        initial_array[index1], initial_array[index2] = initial_array[index2], initial_array[index1]

    elif command[0] == "multiply":
        index1 = int(command[1])
        index2 = int(command[2])
        initial_array[index1] *= initial_array[index2]

    elif command[0] == "decrease":
        initial_array = [int(number) - 1 for number in initial_array]

    command = input().split()

print(", ".join([str(el) for el in initial_array]))
