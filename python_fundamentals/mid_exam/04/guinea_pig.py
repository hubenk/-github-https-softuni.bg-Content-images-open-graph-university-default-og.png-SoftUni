food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000
days = 0
enough_food = True

for _ in range(30):
    days += 1
    food -= 300
    if days % 2 == 0:
        hay -= (food * 0.05)

    if days % 3 == 0:
        cover -= (weight / 3)

    if food <= 0 or hay <= 0 or cover <= 0:
        enough_food = False
        break

food /= 1000
hay /= 1000
cover /= 1000

if enough_food:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print("Merry must go to the pet store!")
