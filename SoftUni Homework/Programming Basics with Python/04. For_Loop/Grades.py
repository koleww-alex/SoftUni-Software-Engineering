number_students = int(input())
student = 0
student_1 = 0
student_2 = 0
student_3 = 0
total_grade = 0
for i in range(1, number_students + 1):
    exam_grade = float(input())

    if 2.00 <= exam_grade <= 2.99:
        student += 1
        total_grade += exam_grade
    elif 3.00 <= exam_grade <= 3.99:
        student_1 += 1
        total_grade += exam_grade
    elif 4.00 <= exam_grade <= 4.99:
        student_2 += 1
        total_grade += exam_grade
    else:
        student_3 += 1
        total_grade += exam_grade

percent_student = (student / number_students) * 100
percent_student_1 = (student_1 / number_students) * 100
percent_student_2 = (student_2 / number_students) * 100
percent_student_3 = (student_3 / number_students) * 100

average_grade = total_grade / number_students

print(f"Top students: {percent_student_3:.2f}%")
print(f"Between 4.00 and 4.99: {percent_student_2:.2f}%")
print(f"Between 3.00 and 3.99: {percent_student_1:.2f}%")
print(f"Fail: {percent_student:.2f}%")
print(f"Average: {average_grade:.2f}")
