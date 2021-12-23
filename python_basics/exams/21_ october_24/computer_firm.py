computers = int(input())
sells = 0
rating = 0
sold = 0
avg_rating = 0

for x in range(computers):
    command = int(input())
    sells = command // 10
    rating = command % 10
    avg_rating += rating
    if rating == 2:
        pass
    elif rating == 3:
       sold += sells * 0.5
    elif rating == 4:
        sold += sells * 0.7
    elif rating == 5:
        sold += sells * 0.85
    elif rating == 6:
        sold += sells * 1

print(f"{sold:.2f}")
print(f"{avg_rating / computers:.2f}")
