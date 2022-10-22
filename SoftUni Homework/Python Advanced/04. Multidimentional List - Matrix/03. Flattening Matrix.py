rows = int(input())
matrix = [[int(i) for i in input().split(', ')] for _ in range(rows)]
flattened = []

for row in matrix:
    flattened.extend(row)

print(flattened)


# Without creating matrix !
flattened = []
for _ in range(rows):
    flattened.extend([int(x) for x in input().split(', ')])

print(flattened)
