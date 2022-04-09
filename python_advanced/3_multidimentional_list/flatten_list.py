random_list = [x for x in input().split("|")]
new_list = []

for _ in range(len(random_list)):
    for x in random_list.pop().split():
        new_list.append(x)

print(*new_list)