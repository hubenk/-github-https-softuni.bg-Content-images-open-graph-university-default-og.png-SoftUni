budget = float(input())
accommodation_number = int(input())
cost = float(input())
others = int(input())

others_expenses = (others / 100 * budget)

if accommodation_number > 7:
    cost *= 0.95

total_expenses = accommodation_number * cost + others_expenses
difference = abs(total_expenses - budget)

if budget >= total_expenses:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")