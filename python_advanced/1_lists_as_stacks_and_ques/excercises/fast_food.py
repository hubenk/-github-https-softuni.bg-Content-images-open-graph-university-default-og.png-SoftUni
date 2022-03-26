from collections import deque

quantity_of_food = int(input())

food_in_orders = deque([int(x) for x in input().split()])

print(max(food_in_orders))

while food_in_orders:

    if food_in_orders[0] <= quantity_of_food:
        quantity_of_food -= food_in_orders[0]
        food_in_orders.popleft()
    else:

        print(f"Orders left: {' '.join(str(x) for x in food_in_orders)}")
        exit()

print("Orders complete")