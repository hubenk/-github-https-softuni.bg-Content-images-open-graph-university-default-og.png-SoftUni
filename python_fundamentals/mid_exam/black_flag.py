pirating = int(input())
plunder_per_day = int(input())
expected_plunder = int(input())
total_plunder = 0

for day in range(1, pirating + 1):

    total_plunder += plunder_per_day

    if day % 3 == 0:
        total_plunder += plunder_per_day / 2

    if day % 5 == 0:
        total_plunder *= 0.7

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percentage_left = (total_plunder / expected_plunder) * 100
    print(f"Collected only {percentage_left:.2f}% of the plunder.")