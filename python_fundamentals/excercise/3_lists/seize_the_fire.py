fire = input().split("#")
water = int(input())
effort = 0
total_fire = 0
print("Cells:")

for cell in fire:
    cell_list = list(cell.split())

    if cell_list[0] == "High" and 81 <= int(cell_list[-1]) <= 125 or cell_list[0] == "Medium" and 51 <= int(cell_list[-1]) <= 80 or cell_list[0] == "Low" and 1 <= int(cell_list[-1]) <= 50:
        water -= int(cell_list[-1])
        if water >= 0:
            effort += int(cell_list[-1]) * 0.25
            total_fire += int(cell_list[-1])
            print(f"- {cell_list[-1]}")
        else:
            water += int(cell_list[-1])

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
