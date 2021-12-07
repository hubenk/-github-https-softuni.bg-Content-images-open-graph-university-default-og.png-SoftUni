record = float(input())
distance = float(input())
time_for_1m = float(input())

Ivans_time = distance * time_for_1m

slow_down = distance // 15 * 12.5       #int(distance / 15);  floor(distance / 15)

Ivans_tottal_time = Ivans_time + slow_down

if_no_record = abs(record - Ivans_tottal_time)

if Ivans_tottal_time < record:
    print(f" Yes, he succeeded! The new world record is {Ivans_tottal_time:.2f} seconds.")

if Ivans_tottal_time >= record:
    print(f"No, he failed! He was {if_no_record:.2f} seconds slower.")