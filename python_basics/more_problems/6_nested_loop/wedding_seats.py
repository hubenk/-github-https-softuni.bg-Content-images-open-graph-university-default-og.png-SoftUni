last_sector = input()
seats_in_1st_sector = int(input())
odd_seats = int(input())
counter_row = 0
counter_seats = 0

for sectors in range(ord("A"), ord(last_sector) + 1):
    for rows in range(1, seats_in_1st_sector + counter_row + 1):
        counter_row += 1
        if counter_row % 2 != 0:
            for seats in range(ord("a"), ord("a") + odd_seats):
                print(f"{chr(sectors)}{rows}{chr(seats)}")
                counter_seats += 1
        else:
            for seats in range(ord("a"), ord("a") + odd_seats + 2):
                print(f"{chr(sectors)}{rows}{chr(seats)}")
                counter_seats += 1
    counter_row = 0
print(counter_seats)
