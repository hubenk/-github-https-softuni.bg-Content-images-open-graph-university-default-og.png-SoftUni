from math import floor
hall_w = float(input()) * 100
hall_h = float(input()) * 100

hall_w_places = floor(hall_w / 120)
hall_h_places = floor((hall_h - 100) / 70)

work_places = hall_h_places * hall_w_places - 3

print(work_places)
