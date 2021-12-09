fuel = str(input())
litres = float(input())

if fuel == "Diesel":
    if litres >= 25:
        print(f"You have enough diesel.")
    else:
        print(f"Fill your tank with diesel!")

elif fuel == "Gas":
    if litres >= 25:
        print(f"You have enough gas.")
    else:
        print(f"Fill your tank with gas!")

elif fuel == "Gasoline":
    if litres >= 25:
        print(f"You have enough gasoline.")
    else:
        print(f"Fill your tank with gasoline!")

else:
    print("Invalid fuel!")