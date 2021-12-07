budget = float(input())
statist = int(input())
statist_dress = float(input())

sum_statist_dress = statist_dress * statist
dekor = budget * 0.1

if statist > 150:
    sum_statist_dress = sum_statist_dress * 0.9     #sum_statist_dress *= 0.9

tottal_expense = sum_statist_dress + dekor

enough_money = budget - tottal_expense
not_enough_money = tottal_expense - budget          #not/enough_money = abs(budget - tottal_expence)

if budget < tottal_expense:
    print(f"Not enough money!")
    print(f"Wingard needs {not_enough_money:.2f} leva more.")

if budget >= tottal_expense:
    print(f"Action!")
    print(f"Wingard starts filming with {enough_money:.2f} leva left.")