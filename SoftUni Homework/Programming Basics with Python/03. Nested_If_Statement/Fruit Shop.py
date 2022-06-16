price = 0
fruit_type = input()
day = input()
quantity = float(input())
condition = True
list_1 = ["Monday","Tuesday"]
if day in list_1 or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit_type == "banana":
        price = quantity * 2.50
    elif fruit_type == "apple":
        price = quantity * 1.20
    elif fruit_type == "orange":
        price = quantity * 0.85
    elif fruit_type == "grapefruit":
        price = quantity * 1.45
    elif fruit_type == "kiwi":
        price = quantity * 2.70
    elif fruit_type == "pineapple":
        price = quantity * 5.50
    elif fruit_type == "grapes":
        price = quantity * 3.85
    else:
        condition = False
elif day == "Saturday" or day == "Sunday":
    if fruit_type == "banana":
        price = quantity * 2.70
    elif fruit_type == "apple":
        price = quantity * 1.25
    elif fruit_type == "orange":
        price = quantity * 0.90
    elif fruit_type == "grapefruit":
        price = quantity * 1.60
    elif fruit_type == "kiwi":
        price = quantity * 3.00
    elif fruit_type == "pineapple":
        price = quantity * 5.60
    elif fruit_type == "grapes":
        price = quantity * 4.20
    else:
        condition = False
else:
    condition = False

if condition:
    print(f"{price:.2f}")
else:
    print("error")
