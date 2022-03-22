number_of_heroes = int(input())
heroes_stats = dict()

for hero in range(number_of_heroes):
    name, hp, mp = input().split()
    heroes_stats[name] = {}
    heroes_stats[name] = [int(hp), int(mp)]

command = input()
while command != "End":
    actions = command.split(" - ")
    hero = actions[1]

    if actions[0] == "CastSpell":
        mana = int(actions[2])
        spell = actions[3]
        if heroes_stats[hero][1] >= mana:
            heroes_stats[hero][1] -= mana
            print(f"{hero} has successfully cast {spell} and now has {heroes_stats[hero][1]} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell}!")

    elif actions[0] == "TakeDamage":
        heroes_stats[hero][0] -= int(actions[2])
        if heroes_stats[hero][0] <= 0:
            print(f"{hero} has been killed by {actions[3]}!")
            del heroes_stats[hero]
        else:
            print(f"{hero} was hit for {actions[2]} HP by {actions[3]} and now has {heroes_stats[hero][0]} HP left!")

    elif actions[0] == "Recharge":
        heroes_stats[hero][1] += int(actions[2])
        if heroes_stats[hero][1] > 200:
            amount_mp = int(actions[2]) - (heroes_stats[hero][1] - 200)
            heroes_stats[hero][1] = 200
            print(f"{hero} recharged for {amount_mp} MP!")
        else:
            print(f"{hero} recharged for {actions[2]} MP!")

    elif actions[0] == "Heal":
        heroes_stats[hero][0] += int(actions[2])
        if heroes_stats[hero][0] > 100:
            amount_hp = int(actions[2]) - (heroes_stats[hero][0] - 100)
            heroes_stats[hero][0] = 100
            print(f"{hero} healed for {amount_hp} HP!")
        else:
            print(f"{hero} healed for {actions[2]} HP!")

    command = input()

for key, value in heroes_stats.items():
    print(key)
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")