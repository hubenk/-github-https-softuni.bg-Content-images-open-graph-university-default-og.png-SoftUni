detergent = int(input())
total_detergent = detergent * 750
utensils = 0
dishes = 0
pots = 0
count = 0

while True:
    dishes_pots = input()

    if dishes_pots == "End":
        print("Detergent was enough!")
        print(f"{dishes} dishes and {pots} pots were washed.")
        print(f"Leftover detergent {total_detergent} ml.")
        break

    count += 1

    if count % 3 == 0:
        pots += int(dishes_pots)
        utensils = int(dishes_pots) * 15
        total_detergent -= utensils

    else:
        dishes += int(dishes_pots)
        utensils = int(dishes_pots) * 5
        total_detergent -= utensils

    if total_detergent <= 0:
        print(f"Not enough detergent, {abs(total_detergent)} ml. more necessary!")
        break
