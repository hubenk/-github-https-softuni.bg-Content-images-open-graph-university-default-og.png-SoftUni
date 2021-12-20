import sys
number = int(input())
average_rating = 0
max_rating = -sys.maxsize
low_rating = sys.maxsize
max_movie = ""
low_movie = ""

for x in range(number):
    movie = input()
    rating = float(input())
    average_rating += rating
    if rating > max_rating:
        max_movie = movie
        max_rating = rating
    if rating < low_rating:
        low_movie = movie
        low_rating = rating

print(f"{max_movie} is with highest rating: {max_rating:.1f}")
print(f"{low_movie} is with lowest rating: {low_rating:.1f}")
print(f"Average rating: {(average_rating / number):.1f}")