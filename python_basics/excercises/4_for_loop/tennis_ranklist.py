from math import floor
tournaments = int(input())
starting_points = int(input())
final_points = starting_points
winnings = 0

for x in range(tournaments):
    stage = str(input())
    if stage == "W":
        final_points += 2000
        winnings += 1
    elif stage == "F":
        final_points += 1200
    elif stage == "SF":
        final_points += 720

average_points = floor((final_points - starting_points) / tournaments)
win_percent = winnings / tournaments * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{win_percent:.2f}%")