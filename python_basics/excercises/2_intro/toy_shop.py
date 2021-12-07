excursion = float(input())
puzzle = int(input())
doll = int(input())
bear = int(input())
minion = int(input())
truck = int(input())

puzzle_sum = puzzle * 2.60
doll_sum = doll * 3
bear_sum = bear * 4.10
minion_sum = minion * 8.20
truck_sum = truck * 2

quantity = puzzle + doll + bear + minion + truck

sum = puzzle_sum + doll_sum + bear_sum + minion_sum + truck_sum

if quantity >= 50:
    sum = sum * 0.75

rent = sum * 0.1

tottal_sum = sum - rent

left_money = tottal_sum - excursion

needed_money = excursion - tottal_sum

if tottal_sum >= excursion:
    print(f"Yes! {left_money:.2f} lv left.")

else:
    print(f"Not enough money! {needed_money:.2f} lv needed.")


