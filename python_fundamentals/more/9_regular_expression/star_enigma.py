import re

messages = int(input())
star_regex = r"[star]|[STAR]"
planet_regex = r"@[A-Z][a-z]+"
population_regex = r":[1-9][0-9]+"
attack_regex = r"![A]!|![D]!"
soldiers_regex = r"->[1-9][0-9]+"
attacked = []
destroyed = []

for msg in range(messages):
    encrypted_strings = input()
    temp_count = 0
    temp_message = ""
    counter = re.findall(star_regex, encrypted_strings)

    for el in encrypted_strings:
        temp_el = ord(el) - len(counter)
        temp_message += chr(temp_el)

    planet = re.finditer(planet_regex, temp_message)
    for _ in planet:
        true_planet = _.group()
        if true_planet:

            population = re.finditer(population_regex, temp_message)
            for _ in population:
                true_population = _.group()
                if true_population:

                    attack = re.finditer(attack_regex, temp_message)
                    for _ in attack:
                        true_attack = _.group()
                        if true_attack:

                            soldiers = re.finditer(soldiers_regex, temp_message)
                            for _ in soldiers:
                                true_soldiers = _.group()
                                if true_soldiers:

                                    if true_attack[1] == "A":
                                        attacked.append(true_planet[1:])
                                    else:
                                        destroyed.append(true_planet[1:])

print(f"Attacked planets: {len(attacked)}")
if len(attacked) > 0:
    for plnt in sorted(attacked, reverse=False):
        print(f"-> {plnt}")

print(f"Destroyed planets: {len(destroyed)}")
if len(destroyed) > 0:

    for plnt in sorted(destroyed, reverse=False):
        print(f"-> {plnt}")
