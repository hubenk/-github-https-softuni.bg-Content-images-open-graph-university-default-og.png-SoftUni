from math import floor
needed_hours = int(input())
days = int(input())
workers_overtime = int(input())

off = days * 0.9
tottal_days = off * 8
extra_hours = workers_overtime * (days * 2)
tottal_worked = floor(extra_hours + tottal_days)
hours_left = abs(tottal_worked - needed_hours)

if tottal_worked >= needed_hours:
    print(f"Yes!{hours_left} hours left.")

else:
    print(f"Not enough time!{hours_left} hours needed.")

