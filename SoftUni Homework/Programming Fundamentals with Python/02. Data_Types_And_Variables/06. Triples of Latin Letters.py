n = int(input())

for x1 in range(1, n + 1):
    for x2 in range(1, n + 1):
        for x3 in range(1, n + 1):

            print(f"{chr(x1 + 96)}{chr(x2 + 96)}{chr(x3 + 96)}")
            