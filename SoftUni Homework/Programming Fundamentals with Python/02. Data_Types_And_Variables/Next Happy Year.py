starting_year = int(input())

found = False

for d1 in range(1, 9 + 1):
    for d2 in range(1, 9 + 1):
        for d3 in range(1, 9 + 1):
            for d4 in range(1, 9 + 1):

                if (d1 * 1000) + (d2 * 100) + (d3 * 10) + d4 >= starting_year:
                    if d1 != d2 and d1 != d3 and d1 != d4:
                        if d2 != d1 and d2 != d3 and d2 != d4:
                            if d3 != d1 and d3 != d2 and d3 != d4:
                                if d4 != d1 and d4 != d2 and d4 != d3:
                                    print(f"{d1}{d2}{d3}{d4}")
                                    found = True
                                    break
                starting_year += 1
        if found:
            break
    if found:
        break
