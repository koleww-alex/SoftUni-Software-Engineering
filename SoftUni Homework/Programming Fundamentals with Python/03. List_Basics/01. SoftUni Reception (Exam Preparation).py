first_employee_handling_customers_per_hour = int(input())
second_employee_handling_customers_per_hour = int(input())
third_employee_handling_customers_per_hour = int(input())

number_of_students = int(input())
total_time_needed = 0
hours_cnt = 0

total_work_per_hour = first_employee_handling_customers_per_hour + second_employee_handling_customers_per_hour +\
                      third_employee_handling_customers_per_hour

for hour in range(1, number_of_students + 1):
    hours_cnt += 1
    if hours_cnt % 4 == 0:
        continue

    number_of_students -= total_work_per_hour

    if number_of_students <= 0:
        break

print(f"Time needed: {hours_cnt}h.")
