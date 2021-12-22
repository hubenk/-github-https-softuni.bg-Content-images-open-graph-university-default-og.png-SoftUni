company = str(input())
senior_ticket = int(input())
junior_tiket = int(input())
price_sen_ticket = float(input())
tax = float(input())

price_jun_ticket = price_sen_ticket * 0.3

total = senior_ticket * price_sen_ticket + junior_tiket * price_jun_ticket

after_tax = (senior_ticket + junior_tiket) * tax

profit = (total + after_tax) * 0.2

print(f"The profit of your agency from {company} tickets is {profit:.2f} lv.")