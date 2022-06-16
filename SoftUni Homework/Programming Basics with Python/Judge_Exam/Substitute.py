k = int(input())
l = int(input())
m = int(input())
n = int(input())

change_cnt = 0
enough_changes = False

for x1 in range(k, 8 + 1):
    for x2 in range(9, l - 1, -1):
        for y1 in range(m, 8 + 1):
            for y2 in range(9, n - 1, -1):

                if x1 % 2 == 0 and y1 % 2 == 0 and x2 % 2 != 0 and y2 % 2 != 0:
                    num1 = x1 * 10 + x2
                    num2 = y1 * 10 + y2

                    if change_cnt == 6:
                        enough_changes = True
                        break
                    if num1 != num2 and num2 != num1:
                        print(f"{x1}{x2} - {y1}{y2}")
                        change_cnt += 1
                    else:
                        print("Cannot change the same player.")
        if enough_changes:
            break
    if enough_changes:
        break
