skumriq_price_per_kg = float(input())
caca_price_per_kg = float(input())

palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input()) * 7.5

palamud_price = skumriq_price_per_kg + skumriq_price_per_kg * 0.6
safrid_price = caca_price_per_kg + caca_price_per_kg * 0.8

total_palamud = palamud_kg * palamud_price
total_safrid = safrid_kg * safrid_price

total = total_safrid + total_palamud + midi_kg

print(f'{total:.2f}')
