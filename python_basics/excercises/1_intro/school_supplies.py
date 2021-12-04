pens = 5.8
markers = 7.2
detergent = 1.2

set_of_pens = int(input()) * pens
set_of_markers = int(input()) * markers
amount_of_detergent = int(input()) * detergent
discount = int(input()) / 100

total_price = set_of_pens + set_of_markers + amount_of_detergent
discount_price = total_price - (total_price * discount)

print(discount_price)