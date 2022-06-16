number_jury = int(input())
total_grade = 0
presentation = input()
presentation_cnt = 0
total_sum = 0
while presentation != "Finish":
    presentation_cnt += 1
    for _ in range(1, number_jury + 1):
        grade = float(input())
        total_grade += grade

    average_grade = total_grade / number_jury
    total_sum += average_grade
    print(f"{presentation} - {average_grade:.2f}.")
    total_grade = 0

    presentation = input()

total_average_grades = total_sum / presentation_cnt
print(f"Student's final assessment is {total_average_grades:.2f}.")
