import sys

initial_list = input().split()
command = input().split()
new_list = list()
initial_length = len(initial_list)
while command[0] != "end":
    temp_list = list()

    if command[0] == "exchange":
        temp_index = int(command[1]) + 1

        if temp_index > len(initial_list):
            print("Invalid index")

        else:
            for index in initial_list[temp_index:]:
                initial_list.append(index)
            for index in initial_list[:temp_index]:
                initial_list.append(index)

            if len(new_list) != initial_length:
                initial_list = initial_list[len(initial_list)//2:]

    elif command[0] == "max":
        if command[1] == "even":
            max_number = -sys.maxsize
            for max in initial_list:
                if int(max) % 2 == 0:
                    if int(max) > int(max_number):
                        max_number = max
            if max_number == -sys.maxsize:
                print("No matches")
            else:
                max_index = initial_list.index(max_number)
                print(max_index)

        elif command[1] == "odd":
            max_number = -sys.maxsize
            for max in initial_list:
                if int(max) % 2 != 0:
                    if int(max) > int(max_number):
                        max_number = max
            if max_number == -sys.maxsize:
                print("No matches")
            else:
                max_index = initial_list.index(max_number)
                print(max_index)

    elif command[0] == "min":
        if command[1] == "even":
            min_number = sys.maxsize
            for min in initial_list:
                if int(min) % 2 == 0:
                    if int(min) < min_number:
                        min_number = int(min)
            if min_number == sys.maxsize:
                print("No matches")
            else:
                min_index = initial_list.index(str(min_number))
                print(min_index)

        elif command[1] == "odd":
            min_number = sys.maxsize
            for min in initial_list:
                if int(min) % 2 != 0:
                    if int(min) < min_number:
                        min_number = int(min)
            if min_number == sys.maxsize:
                print("No matches")
            else:
                min_index = initial_list.index(str(min_number))
                print(min_index)

    elif command[0] == "first" or command[0] == "last":
        if int(command[1]) > len(initial_list):
            print("Invalid count")

        else:
            if command[0] == "first":
                if command[2] == "even":
                    for first in initial_list:
                        if int(first) % 2 == 0:
                            temp_list.append(int(first))
                            if len(temp_list) == int(command[1]):
                                break

                    print(temp_list)
                elif command[2] == "odd":
                    for first in initial_list:
                        if int(first) % 2 != 0:
                            temp_list.append(int(first))
                            if len(temp_list) == int(command[1]):
                                break

                    print(temp_list)
            elif command[0] == "last":
                if command[2] == "even":
                    for last in initial_list[::-1]:
                        if int(last) % 2 == 0:
                            temp_list.append(int(last))
                            if len(temp_list) == int(command[1]):
                                break

                    print(temp_list)

                elif command[2] == "odd":
                    for last in initial_list[::-1]:
                        if int(last) % 2 != 0:
                            temp_list.append(int(last))
                            if len(temp_list) == int(command[1]):
                                break

                    print(temp_list)

    command = input().split()

final_list = [int(x) for x in initial_list]
print(final_list)
