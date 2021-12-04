from math import floor

pages_per_book = int(input())

pages_per_hour = int(input())

days = int(input())

total_time = floor(pages_per_book / pages_per_hour)

total_hours = total_time / days

print(total_hours)
