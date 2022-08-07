info = input().split(" : ")
data_base = {}
while "end" not in info:
    course = info[0]
    name = info[1]

    if course not in data_base:
        data_base[course] = []
    data_base[course].append(name)

    info = input().split(" : ")

for name, info in data_base.items():
    print(f"{name}: {len(data_base[name])}")
    print("\n".join(f"-- {element}" for element in info))
