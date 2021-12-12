number_of_groups = int(input())
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

for x in range(number_of_groups):
    hikers = int(input())
    if hikers <= 5:
        musala += hikers
    elif hikers <= 12:
        monblan += hikers
    elif hikers <= 25:
        kilimandjaro += hikers
    elif hikers <= 40:
        k2 += hikers
    else:
        everest += hikers

tottal_hikers = musala + monblan + kilimandjaro + k2 + everest

musala_perc = musala / tottal_hikers * 100
monblan_perc = monblan / tottal_hikers * 100
kilimandjaro_perc = kilimandjaro / tottal_hikers * 100
k2_perc = k2 / tottal_hikers * 100
everest_perc = everest / tottal_hikers * 100

print(f"{musala_perc:.2f}%")
print(f"{monblan_perc:.2f}%")
print(f"{kilimandjaro_perc:.2f}%")
print(f"{k2_perc:.2f}%")
print(f"{everest_perc:.2f}%")