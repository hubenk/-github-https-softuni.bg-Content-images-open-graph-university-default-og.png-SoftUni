import sys
number = int(input())
max_odd = -sys.maxsize
min_odd = sys.maxsize
max_even = -sys.maxsize
min_even = sys.maxsize
sum_odd = 0
sum_even = 0


for x in range(1,number+1):
    digit = float(input())
    if x % 2 == 0:
        sum_even += digit
        if digit < min_even:
            min_even = digit
        if digit > max_even:
            max_even = digit
    elif x % 2 != 0:
        sum_odd += digit
        if digit < min_odd:
            min_odd = digit
        if digit > max_odd:
            max_odd = digit


print(f"OddSum={sum_odd:.2f},")
if sum_odd == 0:
    print(f"OddMin=No,")
else:
    print(f"OddMin={min_odd:.2f},")
if sum_odd == 0:
    print(f"OddMax=No,")
else:
    print(f"OddMax={max_odd:.2f},")
print(f"EvenSum={sum_even:.2f}")
if sum_even == 0:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={min_even:.2f}")
if sum_even == 0:
    print(f"EvenMax=No,")
else:
    print(f"EvenMax={max_even:.2f},")