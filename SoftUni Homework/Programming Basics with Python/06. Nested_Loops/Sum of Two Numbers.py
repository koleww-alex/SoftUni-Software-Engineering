starting_number = int(input())
ending_number = int(input())
magic_number = int(input())
flag = False
combination_cnt = 0


for i in range(starting_number, ending_number + 1):
    for y in range(starting_number, ending_number + 1):
        combination_cnt += 1
        if i + y == magic_number:
            print(f"Combination N:{combination_cnt} ({i} + {y} = {magic_number})")
            flag = True
            break
    if flag:
        break
if not flag:
    print(f"{combination_cnt} combinations - neither equals {magic_number}")
