lenght_in_sm = int(input())
width_in_sm = int(input())
height_in_sm = int(input())
percentage_others = float(input()) / 100

tank_volume_in_sm = lenght_in_sm * width_in_sm * height_in_sm
volume_litres = tank_volume_in_sm / 1000
total_litres = volume_litres * (1-percentage_others)

print(total_litres)
