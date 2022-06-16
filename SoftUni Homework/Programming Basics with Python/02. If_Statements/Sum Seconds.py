number1 = int(input())
number2 = int(input())
number3 = int(input())
total_time = number1 + number2 + number3
minutes = total_time // 60
seconds = total_time % 60

if seconds <= 9:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
    