guests_number = int(input())
guest_list = set()

for _ in range(guests_number):
    guest_list.add(input())

command = input()

while not command == "END":
    if command in guest_list:
        guest_list.remove(command)

    command = input()

print(len(guest_list))
print('\n'.join(sorted(guest_list)))