from math import floor
record = float(input())
distance = float(input())
time_in_sec_per_1m = float(input())

denivelation = floor(distance / 50) * 30
time = distance * time_in_sec_per_1m + denivelation

if time < record:
    print(f" Yes! The new record is {time:.2f} seconds.")
else:
    print(f"No! He was {time - record:.2f} seconds slower.")
