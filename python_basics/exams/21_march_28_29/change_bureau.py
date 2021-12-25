bitcoin = int(input())
yoan = float(input())
commision = float(input())

bit_eur = ((bitcoin * 1168) / 1.95) * (1 - commision / 100)
yoan_eur = (((yoan * 0.15) * 1.76) / 1.95) * (1 - commision / 100)

print(f"{bit_eur + yoan_eur:.2f}")

