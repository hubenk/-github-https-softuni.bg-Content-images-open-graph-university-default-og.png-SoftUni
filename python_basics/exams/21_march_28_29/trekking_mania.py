number_of_groups = int(input())
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
all_group = 0

for x in range(number_of_groups):
    groups = int(input())

    if groups <= 5:
        musala += groups
        all_group += groups

    elif  groups <= 12:
        monblan += groups
        all_group += groups

    elif groups <= 25:
        kilimandjaro += groups
        all_group += groups

    elif groups <= 40:
        k2 += groups
        all_group += groups
    else:
        everest += groups
        all_group += groups

print(f"{musala/all_group * 100:.2f}%")
print(f"{monblan/all_group * 100:.2f}%")
print(f"{kilimandjaro/all_group * 100:.2f}%")
print(f"{k2/all_group * 100:.2f}%")
print(f"{everest/all_group * 100:.2f}%")
