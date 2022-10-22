from collections import deque
green_light_duration = int(input())
free_window_duration = int(input())
cars = deque()
cars_passed = 0
is_crashed = False
while True:
    command = input()
    current_time = green_light_duration
    if command == 'END':
        print('Everyone is safe.')
        print(f'{cars_passed} total cars passed the crossroads.')
        break
    elif command == 'green':
        while cars:
            passing_car = cars[0]
            time_to_pass = len(passing_car)
            if current_time <= 0:
                break
            if current_time >= time_to_pass:
                current_time -= time_to_pass
                cars.popleft()
                cars_passed += 1
            else:
                time_to_pass -= current_time + free_window_duration
                if time_to_pass > 0:
                    print('A crash happened!')
                    print(f'{passing_car} was hit at {passing_car[-time_to_pass]}.')
                    is_crashed = True
                    break
                else:
                    cars.popleft()
                    cars_passed += 1
                    break
    else:
        cars.append(command)
    if is_crashed:
        break
