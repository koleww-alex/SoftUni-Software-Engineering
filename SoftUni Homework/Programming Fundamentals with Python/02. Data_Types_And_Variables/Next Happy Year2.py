starting_year = int(input())

happy_year = False

while not happy_year:

    starting_year += 1
    set_year = set()

    for i in range(len(str(starting_year))):

        set_year.add(str(starting_year)[i])

    happy_year = len(set_year) == len(str(starting_year))

print(starting_year)
