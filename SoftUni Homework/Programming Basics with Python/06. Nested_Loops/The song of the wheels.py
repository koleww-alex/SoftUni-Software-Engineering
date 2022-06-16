control_num = int(input())

sum_ab = 0
sum_cd = 0
password_cnt = 0
whole_number = 0
password = ""
is_sum_reached_ab = False
is_sum_reached_cd = False
is_the_fourth_wheel = False

for a in range(1, 9 + 1):
    for b in range(1, 9 + 1):
        for c in range(1, 9 + 1):
            for d in range(1, 9 + 1):
                if a < b:
                    sum_ab = a * b
                    is_sum_reached_ab = True
                    if c > d:
                        sum_cd = c * d
                        is_sum_reached_cd = True

                if is_sum_reached_ab and is_sum_reached_cd:
                    if sum_ab + sum_cd == control_num:
                        print(f"{a}{b}{c}{d}", end=" ")
                        password_cnt += 1
                        is_sum_reached_ab = False
                        is_sum_reached_cd = False
                        if password_cnt == 4:
                            is_the_fourth_wheel = True
                            password = f"{a}{b}{c}{d}"
print()

if is_the_fourth_wheel:
    print(f"Password: {password}")
else:
    print("No!")


