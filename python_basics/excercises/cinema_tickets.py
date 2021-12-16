all_student = 0
all_standard = 0
all_kids = 0
all_occupied = 0
movie = input()

while movie != "Finish":
    seats = int(input())
    total_occupied = 0
    occupation = 0
    student = 0
    standard = 0
    kids = 0

    while True:
        tickets = input()


        if tickets == "End":
            all_occupied += total_occupied
            occupation = total_occupied / seats * 100
            print(f"{movie} - {occupation:.2f}% full.")
            movie = input()
            break

        if tickets == "student":
            student += 1
            all_student += 1
            total_occupied += 1
        elif tickets == "standard":
            standard += 1
            all_standard += 1
            total_occupied += 1
        elif tickets == "kid":
            kids += 1
            all_kids += 1
            total_occupied += 1

        if total_occupied >= seats:
            all_occupied += total_occupied
            occupation = total_occupied / seats * 100
            print(f"{movie} - {occupation:.2f}% full.")
            movie = input()
            break

print(f"Total tickets: {all_occupied}")
print(f"{all_student / all_occupied * 100:.2f}% student tickets.")
print(f"{all_standard / all_occupied * 100:.2f}% standard tickets.")
print(f"{all_kids / all_occupied * 100:.2f}% kids tickets.")





