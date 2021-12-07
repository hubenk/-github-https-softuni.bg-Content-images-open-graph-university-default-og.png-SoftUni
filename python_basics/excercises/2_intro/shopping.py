peters_budget = float(input())

#quantity
nvidia = int(input())
memmory = int(input())
pamet = int(input())

#price
vga = 250
tottal_vga = nvidia * vga
tottal_memmory = tottal_vga * 0.35
tottal_pamet = tottal_vga * 0.1

sum_memmory = memmory * tottal_memmory
sum_pamet = pamet * tottal_pamet


tottal = tottal_vga + sum_memmory + sum_pamet

if nvidia > memmory:
    tottal *= 0.85

if peters_budget >= tottal:
    money_left = peters_budget - tottal
    print(f"You have {money_left:.2f} leva left!")

else:
    money_left = tottal - peters_budget
    print(f"Not enough money! You need {money_left:.2f} leva more!")

