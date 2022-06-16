men = int(input())
women = int(input())
table_max_number = int(input())
table_cnt = 0
are_tables_full = False

for m in range(1, men + 1):
    for w in range(1, women + 1):
        table_cnt += 1
        if table_cnt > table_max_number:
            are_tables_full = True
            break
        print(f"({m} <-> {w})", end=" ")
    if are_tables_full:
        break
