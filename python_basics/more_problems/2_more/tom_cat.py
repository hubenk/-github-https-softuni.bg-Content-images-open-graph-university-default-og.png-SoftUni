days_off = int(input())
norma = 30000

off = days_off * 127
on = (365 - days_off) * 63

tottal_minutes = on + off

difference = abs(norma - tottal_minutes)

hours = difference // 60
minutes = difference % 60

if tottal_minutes > norma:
    print(f"Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")

else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")