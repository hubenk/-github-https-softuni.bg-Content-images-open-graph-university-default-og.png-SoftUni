money = float(input())
year = int(input())
age = 17
expense = 0

for x in range(1800, year + 1):
    age += 1
    if x % 2 != 0:
        expense += 12000 + 50 * age
    else:
        expense += 12000

left = abs(money - expense)

if money >= expense:
    print(f"Yes! He will live a carefree life and will have {left:.2f} dollars left.")

else:
    print(f"He will need {left:.2f} dollars to survive.")