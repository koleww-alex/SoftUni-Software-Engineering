number_of_students = int(input())

total_grades = 0

r1 = 0
r2 = 0
r3 = 0
r4 = 0

p1 = 0
p2 = 0
p3 = 0
p4 = 0

for _ in range(1, number_of_students + 1):
    grade = float(input())
    total_grades += grade
    if grade >= 5.00:
        r1 += 1
    elif 4.00 <= grade <= 4.99:
        r2 += 1
    elif 3.00 <= grade <= 3.99:
        r3 += 1
    else:
        r4 += 1

p1 = (r1 / number_of_students) * 100
p2 = (r2 / number_of_students) * 100
p3 = (r3 / number_of_students) * 100
p4 = (r4 / number_of_students) * 100

average_grade = (total_grades / number_of_students)

print(f"Top students: {p1:.2f}%\n"
      f"Between 4.00 and 4.99: {p2:.2f}%\n"
      f"Between 3.00 and 3.99: {p3:.2f}%\n"
      f"Fail: {p4:.2f}%\n"
      f"Average: {average_grade:.2f}")
