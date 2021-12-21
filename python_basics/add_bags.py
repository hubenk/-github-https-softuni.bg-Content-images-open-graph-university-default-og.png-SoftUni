baggage_fair = float(input())
bagage_weight = float(input())
days_till_depart = int(input())
number_of_baggage = int(input())
tax = 0

if bagage_weight < 10:
    tax = baggage_fair * 0.2
elif 10 <= bagage_weight <= 20:
    tax = baggage_fair * 0.5
elif bagage_weight > 20:
    tax = baggage_fair

if days_till_depart < 7:
    tax *= 1.4
elif 7 <= days_till_depart <= 30:
    tax *= 1.15
elif days_till_depart > 30:
    tax *= 1.1

total = number_of_baggage * tax

print(f"The total price of bags is: {total:.2f} lv.")