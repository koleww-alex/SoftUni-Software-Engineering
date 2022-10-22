N, M = tuple(map(int, input().split()))
set_1 = set()
set_2 = set()

for _ in range(N):
    number = input()
    set_1.add(number)

for _ in range(M):
    number = input()
    set_2.add(number)

# set_3 = set_1 & set_2
set_3 = set_1.intersection(set_2)
print('\n'.join(set_3))
