number_of_electrons = int(input())
shells = []
index_counter = 0
while True:
    if number_of_electrons <= 0:
        break

    index_counter += 1
    electron_sum = 2 * (index_counter ** 2)
    last_number_of_electrons = number_of_electrons
    number_of_electrons -= electron_sum
    if number_of_electrons > 0:
        shells.append(electron_sum)
    else:
        shells.append(last_number_of_electrons)


print(shells)
