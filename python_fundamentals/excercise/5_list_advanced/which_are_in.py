first_input = input().split(", ")
second_input = input().split(", ")
substring_list = []

for x in first_input:
    for y in second_input:
        if x in y:
            substring_list.append(x)
            break

print(substring_list)
