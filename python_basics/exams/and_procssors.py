from math import floor
processors = int(input())
workers = int(input())
days = int(input())

working_hours = workers * days * 8
crafted_processors = floor(working_hours / 3)
expected_profit = processors * 110.10
actual_profit = crafted_processors * 110.10

if crafted_processors >= processors:
    print(f"Profit: -> {actual_profit - expected_profit:.2f} BGN")
else:
    print(f"Losses: -> {expected_profit - actual_profit:.2f} BGN")
