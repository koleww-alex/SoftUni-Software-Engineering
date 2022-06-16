def calculating(number):

    if number == 100:
        return f"100% Complete!\n[%%%%%%%%%%]"
    else:
        return f"{number}% [{number // 10 * '%'}{(100 - number) // 10 * '.'}]\nStill loading..."


percents = int(input())

print(calculating(percents))
