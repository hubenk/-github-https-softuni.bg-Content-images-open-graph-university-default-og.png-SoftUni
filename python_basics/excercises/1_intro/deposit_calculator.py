deposit_sum = float(input())

deposit_in_months = int(input())

annual_interest = float(input())

deposit_sum_with_interest = deposit_sum * annual_interest / 100

interest_per_month = deposit_sum_with_interest / 12

total_sum = deposit_sum + deposit_in_months * interest_per_month

print(total_sum)
