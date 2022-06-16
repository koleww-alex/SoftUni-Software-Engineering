number_days = int(input())
number_hours = int(input())

total_sum = 0

for day in range(1, number_days + 1):
    sum_for_the_day = 0

    for hour in range(1, number_hours + 1):

        if day % 2 == 0 and hour % 2 != 0:
            sum_for_the_day += 2.50

        elif day % 2 != 0 and hour % 2 == 0:
            sum_for_the_day += 1.25

        else:
            sum_for_the_day += 1

    print(f"Day: {day} - {sum_for_the_day:.2f} leva")
    total_sum += sum_for_the_day

print(f"Total: {total_sum:.2f} leva")
