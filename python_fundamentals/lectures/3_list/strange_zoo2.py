tail = input()
body = input()
head = input()

arrange = [tail, body, head]

arrange[0], arrange[2] = arrange[2], arrange[0]

print(arrange)
