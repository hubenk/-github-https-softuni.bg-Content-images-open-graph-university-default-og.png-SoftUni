sec_one = set(x for x in input().split())
sec_two = set(x for x in input().split())
lines = int(input())

for _ in range(lines):
    command = input().split()

    if command[0] == "Add":
        for x in range(2, len(command)):
            if command[1] == "First":
                sec_one.add(command[x])
            else:
                sec_two.add(command[x])

    elif command[0] == "Remove":
        for x in range(2, len(command)):
            if command[1] == "First":
                if command[x] in sec_one:
                    sec_one.remove(command[x])
            else:
                if command[x] in sec_two:
                    sec_two.remove(command[x])

    elif command[0] == "Check":
        print(sec_one.issubset(sec_two) or sec_two.issubset(sec_one))

print(*sorted(sec_one), sep=", ")
print(*sorted(sec_two), sep=", ")

