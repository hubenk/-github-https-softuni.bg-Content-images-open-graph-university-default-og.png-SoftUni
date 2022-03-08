sequence_of_el = input().split()
test_el = input().split()
moves = 0
while test_el[0] != "end":

    moves += 1
    index1 = int(test_el[0])
    index2 = int(test_el[1])
    if index1 == index2 or index1 >= len(sequence_of_el) or index2 >= len(sequence_of_el) or index1 < 0 or index2 < 0:
        index = int(len(sequence_of_el) / 2)
        element = f"-{moves}a"
        sequence_of_el.insert(index, element)
        sequence_of_el.insert(index, element)
        print("Invalid input! Adding additional elements to the board")

    else:
        if sequence_of_el[int(test_el[0])] == sequence_of_el[int(test_el[1])]:
            to_be_removed = sequence_of_el[int(test_el[0])]
            sequence_of_el.remove(to_be_removed)
            sequence_of_el.remove(to_be_removed)
            print(f"Congrats! You have found matching elements - {to_be_removed}!")

        else:
            print("Try again!")

    if len(sequence_of_el) == 0:
        print(f"You have won in {moves} turns!")
        exit()

    test_el = input().split()

print("Sorry you lose :(")
print(*sequence_of_el)
