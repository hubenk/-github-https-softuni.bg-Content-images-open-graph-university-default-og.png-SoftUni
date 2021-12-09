fuel = str(input())
litres = float(input())
club_cart = str(input())

gasoline = litres * 2.22
diesel = litres * 2.33
gas = litres * 0.93

gasoline_discount = gasoline - (litres * 0.18)
diesel_discount = diesel - (litres * 0.12)
gas_discount = gas - (litres * 0.08)

if fuel == "Gas":
    if club_cart == "Yes":
        if litres < 20:
            print(f"{gas_discount:.2f} lv.")
        elif 20 <= litres <= 25:
            print(f"{(gas_discount * 0.92):.2f} lv.")
        else:
            print(f"{(gas_discount * 0.9):.2f} lv.")
    elif club_cart == "No":
        if litres < 20:
            print(f"{gas:.2f} lv.")
        elif 20 <= litres <= 25:
            print(f"{(gas * 0.92):.2f} lv.")
        else:
            print(f"{(gas * 0.9):.2f} lv.")

elif fuel == "Gasoline":
    if club_cart == "Yes":
        if litres < 20:
            print(f"{gasoline_discount:.2f} lv.")
        elif 20 <= litres <= 25:
            print(f"{(gasoline_discount * 0.92):.2f} lv.")
        else:
            print(f"{(gasoline_discount * 0.9):.2f} lv.")
    elif club_cart == "No":
        if litres < 20:
            print(f"{gasoline:.2f} lv.")
        elif 20 <= litres <= 25:
            print(f"{(gasoline * 0.92):.2f} lv.")
        else:
            print(f"{(gasoline * 0.9):.2f} lv.")

elif fuel == "Diesel":
    if club_cart == "Yes":
        if litres < 20:
            print(f"{diesel_discount:.2f} lv.")
        elif 20 <= litres <= 25:
            print(f"{(diesel_discount * 0.92):.2f} lv.")
        else:
            print(f"{(diesel_discount * 0.9):.2f} lv.")
    elif club_cart == "No":
        if litres < 20:
            print(f"{diesel:.2f} lv.")
        elif 20 <= litres <= 25:
            print(f"{(diesel * 0.92):.2f} lv.")
        else:
            print(f"{(diesel * 0.9):.2f} lv.")