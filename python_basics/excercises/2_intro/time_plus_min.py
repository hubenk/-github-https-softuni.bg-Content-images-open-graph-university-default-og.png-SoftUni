hours = int(input())
minutes = int(input())

hours_m = hours * 60   #hours
time = hours_m + minutes + 15

new_hours = time // 60
new_minutes = time % 60

if new_hours == 24:
    new_hours = 0

if new_minutes < 10:
    print(f'{new_hours}:0{new_minutes}')   # нулата може и print(f'{new_hours}:{new_minutes:02d}')
else:
    print(f'{new_hours}:{new_minutes}')