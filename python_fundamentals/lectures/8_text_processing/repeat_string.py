string = input().split()
repeated_string = ""

for x in range(len(string)):
     temp_string = string[x] * len(string[x])
     repeated_string += temp_string

print(repeated_string)