interval_start = int(input())
interval_end = int(input())
magic_number = int(input())

combination_cnt = 0

is_magic_number_found = False

for x1 in range(interval_start, interval_end + 1):
    for x2 in range(interval_start, interval_end + 1):
        combination_cnt += 1
        if x1 + x2 == magic_number:
            print(f"Combination N:{combination_cnt} ({x1} + {x2} = {magic_number})")
            is_magic_number_found = True
            break
    if is_magic_number_found:
        break
if not is_magic_number_found:
    print(f"{combination_cnt} combinations - neither equals {magic_number}")
