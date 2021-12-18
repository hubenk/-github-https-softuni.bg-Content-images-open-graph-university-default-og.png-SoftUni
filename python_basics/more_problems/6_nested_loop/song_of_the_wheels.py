input = int(input())
count = 0
password = ""
pass_found = False
over_9 = 0
if input > 10:
    over_9 = 10
else:
    over_9 = input

for a in range(1, over_9):
    for b in range(1, over_9):
        for c in range(1, over_9):
            for d in range(1, over_9):
                if a*b+c*d == input:
                    if a < b and c > d and a < 10 and b < 10 and c < 10 and d < 10:
                        count += 1
                        print(f"{a}{b}{c}{d} ", end="")
                        if count == 4:
                            pass_found = True
                            password = f"{a}{b}{c}{d}"

if pass_found:
    print(f"Password: {password}")
elif pass_found == False:
    print("No!")

