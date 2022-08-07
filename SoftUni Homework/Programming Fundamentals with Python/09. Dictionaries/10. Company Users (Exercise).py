info = input().split(" -> ")
data_base = {}

while "End" not in info:
    company_name = info[0]
    employee_id = info[1]

    if company_name not in data_base:
        data_base[company_name] = []
    if employee_id not in data_base[company_name]:
        data_base[company_name].append(employee_id)

    info = input().split(" -> ")

for key, list_of_value in data_base.items():
    print(key)
    for value in list_of_value:
        print(f"-- {value}")
