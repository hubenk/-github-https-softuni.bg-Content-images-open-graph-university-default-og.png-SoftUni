veggy_price_per_kilo = float(input())
fruit_price_per_kilo = float(input())
tottal_veggy = int(input())
tottal_fruit = int(input())

veggy = veggy_price_per_kilo * tottal_veggy
fruit = fruit_price_per_kilo * tottal_fruit

tottal = (veggy + fruit) / 1.94

print(f'{tottal:.2f}')
