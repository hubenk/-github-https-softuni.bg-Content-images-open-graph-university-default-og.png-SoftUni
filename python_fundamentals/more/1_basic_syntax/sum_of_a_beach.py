string = input().lower()
count = 0

if string.count("sand"):
    count += string.count("sand")
if string.count("water"):
    count += string.count("water")
if string.count("fish"):
    count += string.count("fish")
if string.count("sun"):
    count += string.count("sun")

print(count)
