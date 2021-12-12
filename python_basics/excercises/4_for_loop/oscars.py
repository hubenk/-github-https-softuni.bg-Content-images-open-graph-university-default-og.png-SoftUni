actor = str(input())
points = float(input())
number_of_referees = int(input())
total_points = points

for x in range(number_of_referees):
    name_of_referee = str(input())
    points_of_ref = float(input())
    total_points += len(name_of_referee) * points_of_ref/2
    if total_points > 1250.5:
        break

if total_points > 1250.5:
    print(f"Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!")
else:
    diff = 1250.5 - total_points
    print(f"Sorry, {actor} you need {diff:.1f} more!")