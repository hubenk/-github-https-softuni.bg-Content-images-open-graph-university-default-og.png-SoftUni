square_meters_for_landscaping = float(input())
price_for_square_meter = square_meters_for_landscaping * 7.61
discount = price_for_square_meter * 0.18
total_sum = price_for_square_meter - discount
print(f"The final price is: {total_sum} lv.")
print(f"The discount is: {discount} lv.")