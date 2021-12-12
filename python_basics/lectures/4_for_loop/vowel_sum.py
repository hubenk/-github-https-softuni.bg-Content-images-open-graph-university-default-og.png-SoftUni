text = str(input())
sum = 0

for x in range(0, len(text)):
   if text[x] == "a":
       sum += 1
   if text[x] == "e":
       sum += 2
   if text[x] == "i":
       sum += 3
   if text[x] == "o":
       sum += 4
   if text[x] == "u":
       sum += 5
print(sum)