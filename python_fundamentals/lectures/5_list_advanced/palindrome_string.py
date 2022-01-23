words = input().split()
palindrome = input()
count = 0
palindrome_list = []

for x in words:
    result = "".join(reversed(x))     #x[::-1]
    if result == x:
        palindrome_list.append(result)


print(palindrome_list)
print(f"Found palindrome {words.count(palindrome)} times")
