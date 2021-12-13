stadium_capacy = int(input())
number_of_fans = int(input())
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for x in range(number_of_fans):
    sector = str(input())
    if sector == "A":
        sector_a += 1
    elif sector == "B":
        sector_b += 1
    elif sector == "V":
        sector_v += 1
    elif sector == "G":
        sector_g += 1

percnt_a = sector_a / number_of_fans * 100
percnt_b = sector_b / number_of_fans * 100
percnt_v = sector_v / number_of_fans * 100
percnt_g = sector_g / number_of_fans * 100
occupacy = (sector_a + sector_b + sector_v + sector_g) / stadium_capacy * 100

print(f"{percnt_a:.2f}%")
print(f"{percnt_b:.2f}%")
print(f"{percnt_v:.2f}%")
print(f"{percnt_g:.2f}%")
print(f"{occupacy:.2f}%")
