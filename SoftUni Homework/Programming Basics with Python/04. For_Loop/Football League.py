stadium_capacity = int(input())
number_fans = int(input())

r1 = 0
r2 = 0
r3 = 0
r4 = 0

for _ in range(1, number_fans + 1):
    sector = input()

    if sector == "A":
        r1 += 1
    elif sector == "B":
        r2 += 1
    elif sector == "V":
        r3 += 1
    else:
        r4 += 1

p1 = (r1 / number_fans) * 100
p2 = (r2 / number_fans) * 100
p3 = (r3 / number_fans) * 100
p4 = (r4 / number_fans) * 100

p_stadium = (number_fans / stadium_capacity) * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p_stadium:.2f}%")
