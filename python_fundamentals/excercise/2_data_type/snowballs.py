snowballs = int(input())
highest_value = 0
the_best_ball = ""

for ball in range(snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight/time) ** quality

    if value > highest_value:
        highest_value = value
        the_best_ball = f"{weight} : {time} = {highest_value:.0f} ({quality})"

print(the_best_ball)
