number_coins_1_lev = int(input())
number_coins_2_leva = int(input())
number_coins_5_leva = int(input())

final_sum = int(input())

for x1 in range(0, number_coins_1_lev + 1):
    first_sum = x1 * 1
    for x2 in range(0, number_coins_2_leva + 1):
        second_sum = x2 * 2
        for x3 in range(0, number_coins_5_leva + 1):
            third_sum = x3 * 5
            if first_sum + second_sum + third_sum == final_sum:
                print(f"{x1} * 1 lv. + {x2} * 2 lv. + {x3} * 5 lv. = {final_sum} lv.")
