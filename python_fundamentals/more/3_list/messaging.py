number_line = input().split(" ")
string_list = list(input())
output = ""
index = 0

for x in number_line:
    x = map(int, x)
    index = sum(x)

    while True:
        if index >= len(string_list):
            index -= len(string_list)

        if index < len(string_list):
            output += string_list[index]
            string_list.remove(string_list[index])
            break

print(output)


