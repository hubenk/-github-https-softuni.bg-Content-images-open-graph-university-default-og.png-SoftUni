version = input().split(".")
list_version = [int(number) for number in version]
list_version[2] += 1

if list_version[2] == 10:
    list_version[2] = 0
    list_version[1] += 1

if list_version[1] == 10:
    list_version[1] = 0
    list_version[0] += 1

new_version = [str(number) for number in list_version]

print(".".join(new_version))
