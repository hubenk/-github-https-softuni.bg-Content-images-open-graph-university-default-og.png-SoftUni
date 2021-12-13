period = int(input())
treated = 0
untreated = 0


for x in range(1, period + 1):
    patients_per_day = int(input())

    if x < 3:
        if patients_per_day >= 7:
            treated += 7
            untreated += patients_per_day - 7
        else:
            treated += patients_per_day
    elif x >= 3:
        if untreated > treated:
            if patients_per_day >= 8:
                treated += 8
                untreated += patients_per_day - 8
            else:
                treated += patients_per_day
        elif treated > untreated:
            if patients_per_day >= 7:
                treated += 7
                untreated += patients_per_day - 7
            else:
                treated += patients_per_day

print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")