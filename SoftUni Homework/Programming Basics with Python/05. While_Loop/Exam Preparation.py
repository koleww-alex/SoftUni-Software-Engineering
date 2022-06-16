poor_grades = int(input())
exercise_name = input()
poor_grades_cnt = 0
total_grades = 0
total_grades_cnt = 0
exercise_name_cnt = 0
last_exercise = ""

while exercise_name != "Enough":
    grade = int(input())
    total_grades_cnt += 1
    total_grades += grade
    exercise_name_cnt += 1
    if grade <= 4:
        poor_grades_cnt += 1
        if poor_grades_cnt == poor_grades:
            print(f"You need a break, {poor_grades_cnt} poor grades.")
            break

    exercise_name = input()

    if exercise_name != "Enough":
        last_exercise = exercise_name

average_score = total_grades / total_grades_cnt

if exercise_name == "Enough":
    print(f"Average score: {average_score:.2f}\n"
          f"Number of problems: {exercise_name_cnt}\n"
          f"Last problem: {last_exercise}")
