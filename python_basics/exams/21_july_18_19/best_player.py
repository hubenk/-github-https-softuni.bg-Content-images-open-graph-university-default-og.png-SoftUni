command = input()
score = 0
player = ""

while command != "END":
    goals = int(input())

    if goals > score:
        score = goals
        player = command
    if goals >= 10:
        break
    command = input()

if score >= 3:
    print(f"{player} is the best player!")
    print(f"He has scored {score} goals and made a hat-trick !!!")
else:
    print(f"{player} is the best player!")
    print(f"He has scored {score} goals.")



