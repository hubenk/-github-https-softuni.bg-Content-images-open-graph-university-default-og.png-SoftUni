city = input()
volume = float(input())
commission = 0


if city == "Sofia":
    if 0 <= volume <= 500:
        commission = 0.05
    elif 500 < volume <= 1000:
        commission = 0.07
    elif 1000 < volume <= 10000:
        commission = 0.08
    elif volume > 10000:
        commission = 0.12

elif city == "Varna":
    if 0 <= volume <= 500:
        commission = 0.045
    elif 500 < volume <= 1000:
        commission = 0.075
    elif 1000 < volume <= 10000:
        commission = 0.10
    elif volume > 10000:
        commission = 0.13

elif city == "Plovdiv":
    if 0 <= volume <= 500:
        commission = 0.055
    elif 500 < volume <= 1000:
        commission = 0.08
    elif 1000 < volume <= 10000:
        commission = 0.12
    elif volume > 10000:
        commission = 0.145

tottal = volume * commission

if tottal > 0:
    print(f"{tottal:.2f}")

else:
    print("error")







