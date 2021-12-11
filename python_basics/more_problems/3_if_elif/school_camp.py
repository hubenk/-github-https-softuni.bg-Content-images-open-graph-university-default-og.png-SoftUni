season = str(input())
gender = str(input())
number_of_students = int(input())
number_of_nights = int(input())
sport = ""
price = 0

if gender == "boys" or gender == "girls":
    if season == "Winter":
        price = (number_of_nights * 9) * number_of_students
    elif season == "Spring":
        price = (number_of_nights * 7.2) * number_of_students
    elif season == "Summer":
        price = (number_of_nights * 15) * number_of_students

elif gender == "mixed":
    if season == "Winter":
        price = (number_of_nights * 10) * number_of_students
    elif season == "Spring":
        price = (number_of_nights * 9.5) * number_of_students
    elif season == "Summer":
        price = (number_of_nights * 20) * number_of_students
    if season == "Winter":
        sport = "Ski"
    elif season == "Spring":
        sport = "Cycling"
    elif season == "Summer":
        sport = "Swimming"

if gender == "boys":
    if season == "Winter":
        sport = "Judo"
    elif season == "Spring":
        sport = "Tennis"
    elif season == "Summer":
        sport = "Football"
elif gender == "girls":
    if season == "Winter":
        sport = "Gymnastics"
    elif season == "Spring":
        sport = "Athletics"
    elif season == "Summer":
        sport = "Volleyball"

if number_of_students >= 50:
    price *= 0.5
elif 50 > number_of_students >= 20:
    price *= 0.85
elif 20 > number_of_students >= 10:
    price *= 0.95

print(f"{sport} {price:.2f} lv.")