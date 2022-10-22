from collections import deque

seats = input().split(', ')
first_sequence = deque(map(int, input().split(', ')))
second_sequence = deque(map(int, input().split(', ')))
taken_seats = []
rotations = 0

while rotations < 10 and len(taken_seats) < 3:
    rotations += 1
    first_number = first_sequence.popleft()
    second_number = second_sequence.pop()
    ch = chr(first_number + second_number)

    first_seat, second_seat = str(first_number) + ch, str(second_number) + ch

    if first_seat in taken_seats or second_seat in taken_seats:
        continue

    elif first_seat in seats:
        taken_seats.append(first_seat)

    elif second_seat in seats:
        taken_seats.append(second_seat)

    else:
        first_sequence.append(first_number)
        second_sequence.appendleft(second_number)


print(f'Seat matches: {", ".join(taken_seats)}')
print(f'Rotations count: {rotations}')
