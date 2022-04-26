class ValueCannotBeNegative(Exception):
    """"Number cannot be under 0!"""

    
for num in range(5):
    number = int(input())
    if number >= 0:
        pass
    else:
        raise ValueCannotBeNegative

