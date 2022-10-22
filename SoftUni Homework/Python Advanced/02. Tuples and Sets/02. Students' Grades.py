number_of_iterations = int(input())
students_info = {}
for _ in range(number_of_iterations):
    name, grade = input().split()
    if name not in students_info:
        students_info[name] = []
    students_info[name].append(float(grade))

for name, grades in students_info.items():
    average_grade = sum(grades) / len(grades)
    grades_list = " ".join(str(f'{grade:.2f}') for grade in grades)
    print(f'{name} -> {grades_list} (avg: {average_grade:.2f})')

