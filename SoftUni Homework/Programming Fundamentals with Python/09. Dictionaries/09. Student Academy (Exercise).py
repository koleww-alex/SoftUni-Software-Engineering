number_of_grades = int(input())
data_base = {}
for _ in range(number_of_grades):
    name = input()
    grade = float(input())
    if name not in data_base:
        data_base[name] = []
    data_base[name].append(grade)

print("\n".join(f"{name} -> {sum(value) / len(value):.2f}"
                for name, value in data_base.items() if sum(value) / len(value) >= 4.50))
