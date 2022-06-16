number_groups = int(input())

people = 0
total_people = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0


for i in range(1, number_groups + 1):
    people = int(input())
    total_people += people
    if people <= 5:
        p1 += people
    elif 6 <= people <= 12:
        p2 += people
    elif 13 <= people <= 25:
        p3 += people
    elif 26 <= people <= 40:
        p4 += people
    else:
        p5 += people


percent_p1 = (p1 / total_people) * 100
percent_p2 = (p2 / total_people) * 100
percent_p3 = (p3 / total_people) * 100
percent_p4 = (p4 / total_people) * 100
percent_p5 = (p5 / total_people) * 100

print(f"{percent_p1:.2f}%")
print(f"{percent_p2:.2f}%")
print(f"{percent_p3:.2f}%")
print(f"{percent_p4:.2f}%")
print(f"{percent_p5:.2f}%")
