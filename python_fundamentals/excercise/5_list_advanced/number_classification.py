number = input().split(", ")
positive = []
negative = []
even = []
odd = []

pos_neg = [positive.append(x) if int(x) >= 0 else negative.append(x) for x in number]
even_odd = [even.append(y) if int(y) % 2 == 0 else odd.append(y) for y in number]

positive_no_brackets = ", ".join(positive)
negative_no_brackets = ", ".join(negative)
even_no_brackets = ", ".join(even)
odd_no_brackets = ", ".join(odd)

print(f"Positive: {positive_no_brackets}")
print(f"Negative: {negative_no_brackets}")
print(f"Even: {even_no_brackets}")
print(f"Odd: {odd_no_brackets}")