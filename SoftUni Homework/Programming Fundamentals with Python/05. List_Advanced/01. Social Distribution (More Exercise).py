population = list(map(int, input().split(", ")))
minimum_wealth = int(input())
population.sort()
is_it_possible = True
current_biggest_number = max(population)
for i in range(len(population)):
    if population[-1] < minimum_wealth:
        print("No equal distribution possible")
        is_it_possible = False
        break
    if population[-1] > population[-2]:
        if population[i] < minimum_wealth:
            population[-1] -= (minimum_wealth - population[i])
            population[i] = minimum_wealth

    elif population[-2] > population[-3]:
        if population[i] < minimum_wealth:
            population[-2] -= (minimum_wealth - population[i])
            population[i] = minimum_wealth
    else:
        if population[i] < minimum_wealth:
            population[-3] -= (minimum_wealth - population[i])
            population[i] = minimum_wealth

if is_it_possible:
    print(population)
