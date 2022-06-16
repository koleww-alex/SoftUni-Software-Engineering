start_interval = int(input())
end_interval = int(input())

is_number_special = False

for first_num in range(start_interval, end_interval + 1):
    for second_num in range(start_interval, end_interval + 1):
        for third_num in range(start_interval, end_interval + 1):
            for fourth_num in range(start_interval, end_interval + 1):

                if first_num % 2 == 0 and fourth_num % 2 != 0:
                    num_sum = second_num + third_num
                    if first_num > fourth_num and num_sum % 2 == 0:
                        is_number_special = True

                elif first_num % 2 != 0 and fourth_num % 2 == 0:
                    num_sum = second_num + third_num
                    if first_num > fourth_num and num_sum % 2 == 0:
                        is_number_special = True

                if is_number_special:
                    is_number_special = False
                    print(f"{first_num}{second_num}{third_num}{fourth_num}", end=" ")

