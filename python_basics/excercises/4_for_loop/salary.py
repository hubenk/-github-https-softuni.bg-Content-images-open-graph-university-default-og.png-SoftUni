tabs_number = int(input())
salary = float(input())
fine = 0

for x in range(0, tabs_number):
    web = str(input())
    if web == "Facebook":
        fine += 150
    elif web == "Instagram":
        fine += 100
    elif web == "Reddit":
        fine += 50


diff = salary - fine

if salary > fine:
    print(f"{diff:.0f}")
else:
    print("You have lost your salary.")