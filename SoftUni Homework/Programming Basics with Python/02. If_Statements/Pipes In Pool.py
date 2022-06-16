v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())
water = (p1 + p2) * h

percent_liters = water / v * 100
pipe1_percent = (p1 * h) / water * 100
pipe2_percent = (p2 * h) / water * 100

if water <= v:
    print(f"The pool is {percent_liters}% full. Pipe 1: {pipe1_percent:.2f}%. Pipe 2: {pipe2_percent:.2f}%")
else:
    print(f"For {h} hours the pool overflows with {water - v} liters")
