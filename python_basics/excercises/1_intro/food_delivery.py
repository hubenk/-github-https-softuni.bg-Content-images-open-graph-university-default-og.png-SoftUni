chiken_menu = int(input()) * 10.35
fish_menu = int(input()) * 12.40
veggy_menu = int(input()) * 8.15

desert = (chiken_menu + fish_menu + veggy_menu) * 0.2

food_delivery = 2.5

total_delivery = chiken_menu + fish_menu + veggy_menu + desert + food_delivery

print(total_delivery)