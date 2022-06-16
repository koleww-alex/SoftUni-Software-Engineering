number_turns = int(input())
points = 0
r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0
r6 = 0
for _ in range(1, number_turns + 1):
    new_number = int(input())

    if 0 <= new_number <= 9:
        points += new_number * 0.2
        r1 += 1
    elif 10 <= new_number <= 19:
        points += new_number * 0.3
        r2 += 1
    elif 20 <= new_number <= 29:
        points += new_number * 0.4
        r3 += 1
    elif 30 <= new_number <= 39:
        points += 50
        r4 += 1
    elif 40 <= new_number <= 50:
        points += 100
        r5 += 1
    else:
        points /= 2
        r6 += 1

p1 = (r1 / number_turns) * 100
p2 = (r2 / number_turns) * 100
p3 = (r3 / number_turns) * 100
p4 = (r4 / number_turns) * 100
p5 = (r5 / number_turns) * 100
p6 = (r6 / number_turns) * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {p1:.2f}%\n"
      f"From 10 to 19: {p2:.2f}%\n"
      f"From 20 to 29: {p3:.2f}%\n"
      f"From 30 to 39: {p4:.2f}%\n"
      f"From 40 to 50: {p5:.2f}%\n"
      f"Invalid numbers: {p6:.2f}%")
