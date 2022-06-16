n = int(input())

for thousands in range(1, 9 + 1):
    for hundreds in range(1, 9 + 1):
        for tens in range(1, 9 + 1):
            for num in range(1, 9 + 1):
                first_sum = thousands + hundreds
                second_sum = tens + num
                if first_sum == second_sum and n % first_sum == 0:
                    print(f"{thousands}{hundreds}{tens}{num}", end=" ")
