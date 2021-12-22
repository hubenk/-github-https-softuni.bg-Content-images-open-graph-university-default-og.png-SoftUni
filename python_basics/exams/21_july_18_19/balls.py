from math import floor

number = int(input())
red = 0
orange = 0
yellow = 0
white = 0
black = 0
others = 0
total_point = 0

for x in range(number):
    color = input()

    if color == "red":
        total_point += 5
        red += 1
    elif color == "orange":
        total_point += 10
        orange += 1
    elif color == "yellow":
        total_point += 15
        yellow += 1
    elif color == "white":
        total_point += 20
        white += 1
    elif color == "black":
        total_point = floor(total_point / 2)
        black += 1
    else:
        others += 1

print(f"Total points: {total_point}")
print(f"Points from red balls: {red}")
print(f"Points from orange balls: {orange}")
print(f"Points from yellow balls: {yellow}")
print(f"Points from white balls: {white}")
print(f"Other colors picked: {others}")
print(f"Divides from black balls: {black}")

