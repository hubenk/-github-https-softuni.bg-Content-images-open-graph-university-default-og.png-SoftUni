juniors = int(input())
seniors = int(input())
trace = str(input())
kids = juniors + seniors
jun_tax = 0
sen_tax = 0

if trace == "trail":
    jun_tax = 5.50
    sen_tax = 7
elif trace == "cross-country":
    jun_tax = 8
    sen_tax = 9.50
elif trace == "downhill":
    jun_tax = 12.25
    sen_tax = 13.75
elif trace == "road":
    jun_tax = 20
    sen_tax = 21.50

if trace == "cross-country" and kids >= 50:
    sum = ((juniors * jun_tax) + (sen_tax * seniors)) * 0.75
else:
    sum = (juniors * jun_tax) + (sen_tax * seniors)

sum *= 0.95

print(f"{sum:.2f}")

