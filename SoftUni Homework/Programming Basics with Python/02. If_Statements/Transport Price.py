km = int(input())
day_night = input()

if 20 <= km < 100:
    autobus = km * 0.09
    print(f'{autobus:.2f}')

elif 100 <= km:
    train = km * 0.06
    print(f'{train:.2f}')
else:
    if day_night == 'day':
        entry_tax = 0.7
        taxi_day = (km * 0.79) + entry_tax
        print(f'{taxi_day:.2f}')
    else:
        entry_tax = 0.7
        taxi_night = (km * 0.9) + entry_tax
        print(f'{taxi_night:.2f}')

