from math import pi

figure = input()

if figure == "square":
    area_1 = float(input())
    tottal_area = area_1 * area_1
    print(f'{tottal_area:.3f}')

elif figure == "rectangle":
    area_1 = float(input())
    area_2 = float(input())
    tottal_area = area_1 * area_2
    print(f'{tottal_area:.3f}')

elif figure == "circle":
    area_1 = float(input())
    tottal_area = pi * area_1**2
    print(f'{tottal_area:.3f}')

elif figure == "triangle":
    area_1 = float(input())
    area_2 = float(input())
    tottal_area = area_1 * area_2 / 2
    print(f'{tottal_area:.3f}')


