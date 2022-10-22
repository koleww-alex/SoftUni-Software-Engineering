rows = int(input())
matrix = [[int(i) for i in input().split(', ') if int(i) % 2 == 0] for _ in range(rows)]
print(matrix)
