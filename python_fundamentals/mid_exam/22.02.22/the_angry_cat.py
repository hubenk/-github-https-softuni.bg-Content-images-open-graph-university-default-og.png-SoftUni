price_rating = [int(x) for x in input().split(", ")]
entry = int(input())
command = input()
position = ""
sum_left = 0
sum_right = 0
biggest_ratings = 0

for left in range(entry):
    if command == "cheap":
        if price_rating[left] < price_rating[entry]:
            sum_left += price_rating[left]
    else:
        if price_rating[left] >= price_rating[entry]:
            sum_left += price_rating[left]

for right in range(entry + 1, len(price_rating)):
    if command == "cheap":
        if price_rating[right] < price_rating[entry]:
            sum_right += price_rating[right]
    else:
        if price_rating[right] >= price_rating[entry]:
            sum_right += price_rating[right]

if sum_right > sum_left:
    position = "Right"
    biggest_ratings = sum_right
else:
    position = "Left"
    biggest_ratings = sum_left

print(f"{position} - {biggest_ratings}")
