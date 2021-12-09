from math import ceil, floor
magnolii_br = int(input())
zumbuli_br = int(input())
roses_br = int(input())
cactus_br = int(input())
present = float(input())

magnolii = magnolii_br * 3.25
zumbuli = zumbuli_br * 4
roses = roses_br * 3.50
cactus = cactus_br * 8

including_tax = (magnolii + zumbuli + roses + cactus) * 0.95

enough = floor(including_tax - present)
not_enough = ceil(present - including_tax)

if including_tax >= present:
    print(f"She is left with {enough} leva.")

else:
    print(f"She will have to borrow {not_enough} leva.")