from math import floor

biscuits_per_day = int(input())
workers = int(input())
competition_biscuits_per_30_day = int(input())
total_biscuits = 0

for day in range(1, 31):
    if day % 3 == 0:
        temp_bisc = floor((biscuits_per_day * 0.75) * workers)
        total_biscuits += temp_bisc
    else:
        total_biscuits += (biscuits_per_day * workers)

print(f"You have produced {total_biscuits} biscuits for the past month.")

if total_biscuits > competition_biscuits_per_30_day:
    difference = ((total_biscuits - competition_biscuits_per_30_day) / competition_biscuits_per_30_day) * 100
    print(f"You produce {difference:.2f} percent more biscuits.")
else:
    difference = ((competition_biscuits_per_30_day - total_biscuits) / competition_biscuits_per_30_day) * 100
    print(f"You produce {difference:.2f} percent less biscuits.")