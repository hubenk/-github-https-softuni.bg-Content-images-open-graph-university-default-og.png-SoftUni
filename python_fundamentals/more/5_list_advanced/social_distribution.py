population = [int(people) for people in input().split(", ")]
sorted_population = sorted(population)
minimum_wealth = int(input())
raise_money = 0
max_index = len(population) -1
max_number = sorted_population[max_index]

for index, people in enumerate(population):
    if index == max_index:
        population[index] = max_number
        print(population)
        break

    if people < minimum_wealth:
        raise_money = minimum_wealth - people

        if max_number - raise_money < minimum_wealth:
            population[max_index] = max_number
            max_index -= 1
            max_number = sorted_population[max_index]
        if max_number < minimum_wealth:
            print("No equal distribution possible")
            exit()

        max_number -= raise_money
        population[index] = minimum_wealth

