fats = int(input())
proteins = int(input())
carbs = int(input())
calories = int(input())
water = int(input())

total_fats = ((fats / 100) * calories) / 9
total_protein = ((proteins / 100) * calories) / 4
total_carbs = ((carbs / 100) * calories) / 4

weight = total_fats + total_protein + total_carbs

total = (calories / weight) * ((100 - water) / 100)

print(f"{total:.4f}")
