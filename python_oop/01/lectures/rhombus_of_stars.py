def rhombus(counter):
    for x in range(1, counter + 1):
        print(" " * (counter - x) + "* " * x)
    for x in range(counter - 1, 0, -1):
        print(" " * (counter - x) + "* " * x)


pos_integer = int(input())

rhombus(pos_integer)
