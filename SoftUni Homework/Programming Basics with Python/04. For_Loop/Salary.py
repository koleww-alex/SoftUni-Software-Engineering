# input

number_open_tabs = int(input())
salary = int(input())
current_website = ""

# action

for _ in range(1, number_open_tabs + 1):
    n = input()
    if n == "Facebook":
        salary -= 150
    elif n == "Instagram":
        salary -= 100
    elif n == "Reddit":
        salary -= 50

# output
    if salary <= 0:
        print("You have lost your salary.")
        break
else:
    print(f"{salary}")
