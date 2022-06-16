name = input()
years_count = 0
failed_years = 0
total_grades = 0

while True:
    year_grade = float(input())
    years_count += 1
    if year_grade < 4.00:
        failed_years += 1
        if failed_years == 2:
            print(f"{name} has been excluded at {years_count} grade")
            break
        years_count -= 1
    else:
        total_grades += year_grade

    if years_count == 12:
        average_grade = total_grades / 12
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break
