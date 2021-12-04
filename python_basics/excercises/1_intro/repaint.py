nylon = (int(input()) + 2) * 1.5
paint = int(input()) * 14.50
desolve_paint = int(input()) * 5
labor_per_hour = int(input())

nylon_bags = 0.4
paint_plus = paint * 0.1

total_paint = paint + paint_plus
labor = (nylon + nylon_bags + desolve_paint + total_paint) * 0.3
total_labor = labor_per_hour * labor


print(nylon + total_paint + desolve_paint + total_labor +  nylon_bags)