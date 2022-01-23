command = input()
to_do_list = [0] * 10
while command != "End":

    index, priority = command.split("-")
    current_index = int(index) - 1
    to_do_list[int(current_index)] = priority

    command = input()

print([x for x in to_do_list if x != 0])
