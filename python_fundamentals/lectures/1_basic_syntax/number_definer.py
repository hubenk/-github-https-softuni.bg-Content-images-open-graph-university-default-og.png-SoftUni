number = float(input())
definition = ""

if number == 0:
    definition = "zero"
elif number > 0:
    definition = "positive"
elif number < 0:
    definition = "negative"

if number == 0:
    print(definition)
elif abs(number) < 0:
    print(f"small {definition}")
elif abs(number) > 1000000:
    print(f"large {definition}")
else:
    print(definition)
