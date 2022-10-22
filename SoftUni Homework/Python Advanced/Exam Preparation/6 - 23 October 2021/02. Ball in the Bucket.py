SIZE = 6
matrix = [input().split() for _ in range(SIZE)]
points_scored = 0
prizes = {
    'Lego Construction Set': [300],
    'Teddy Bear': [200, 299],
    'Football': [100, 199],

}
prize_achieved = ''
for _ in range(3):
    row, col = list(map(int, input().strip('()').split(', ')))

    if 0 <= row < SIZE and 0 <= col < SIZE:
        if matrix[row][col] == 'B':
            matrix[row][col] = '.'
            for i in range(1, SIZE):
                if not 0 <= row + i < SIZE:
                    break
                points_scored += int(matrix[row + i][col])

            for i in range(1, SIZE):
                if not 0 <= row - i < SIZE:
                    break
                points_scored += int(matrix[row - i][col])

for item in prizes:
    if len(prizes[item]) == 1:
        if points_scored >= prizes[item][0]:
            prize_achieved = item
            break
    else:
        if prizes[item][0] <= points_scored <= prizes[item][1]:
            prize_achieved = item
            break

if not prize_achieved:
    print(f'Sorry! You need {100 - points_scored} points more to win a prize.')
else:
    print(f"Good job! You scored {points_scored} points, and you've won {prize_achieved}.")
