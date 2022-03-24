brackets = [x for x in input()]
left_brackets = []
right_brackets = []
parentheses = True

for el in brackets:
    if el == "(" or el == "[" or el == "{":
        left_brackets.append(el)
    else:
        if el == ")":
            right_brackets.append("(")
        elif el == "]":
            right_brackets.append('[')
        elif el == "}":
            right_brackets.append("{")

if left_brackets == right_brackets[::-1]:
    print("YES")
elif left_brackets == right_brackets:
    print("YES")
else:
    print("NO")
