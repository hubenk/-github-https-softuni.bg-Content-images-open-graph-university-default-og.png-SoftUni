exam_h = int(input())
exam_m = int(input())
arrive_h = int(input())
arrive_m = int(input())

exam = (exam_h * 60) + exam_m
arrive = (arrive_h * 60) + arrive_m

difference = abs(exam - arrive)
h = difference // 60
m = difference % 60

if arrive > exam:
    if difference >= 60:
        print("Late")
        print(f"{h}:{m:02d} hours after the start")
    else:
        print("Late")
        print(f"{m} minutes after the start")

elif difference == 0:
    print("On time")

elif 0 <= difference <= 30:
    print("On time")
    print(f"{m} minutes before the start")

elif 30 < difference < 60:
    print("Early")
    print(f"{m} minutes before the start")

elif difference >= 60:
    print("Early")
    print(f"{h}:{m:02d} hours before the start")
