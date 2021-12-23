party_cost = float(input())
love_messages = int(input())
roses = int(input())
key_chains = int(input())
caricatures = int(input())
lucks = int(input())

love = love_messages * 0.60
rose = roses * 7.20
key = key_chains * 3.60
cari = caricatures * 18.20
luck = lucks * 22

total = love + rose + key + cari + luck
number = love_messages + roses + key_chains + caricatures + lucks

if number > 25:
    total *= 0.65

total *= 0.9

if total > party_cost:
    print(f"Yes! {total - party_cost:.2f} lv left.")
else:
    print(f"Not enough money! {party_cost - total:.2f} lv needed.")