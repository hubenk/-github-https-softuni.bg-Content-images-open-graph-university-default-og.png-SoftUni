time1 = int(input())
time2 = int(input())
time3 = int(input())

tottal_time = time1 + time2 + time3

minutes = tottal_time //60
seconds = tottal_time % 60

time = (f'{minutes}:{seconds}')

if seconds < 10:
    print(f'{minutes}:0{seconds}') # кратък вариант без if/else print(f'{minutes}:{seconds:02d}')
else:
    print(time)