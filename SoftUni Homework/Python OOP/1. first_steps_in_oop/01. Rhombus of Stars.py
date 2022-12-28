def create_row():
    print((N - row) * ' ', end='')
    for col in range(row):
        print('*', end=' ')
    print()


N = int(input())
for row in range(1, N + 1):
    create_row()

for row in range(N - 1, -1, -1):
    create_row()
