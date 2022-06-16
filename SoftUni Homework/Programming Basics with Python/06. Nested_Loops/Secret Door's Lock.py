upper_border_hundreds = int(input())
upper_border_tens = int(input())
upper_border_nums = int(input())

list1 = [2, 3, 5, 7]

for hundreds in range(1, upper_border_hundreds + 1):
    for tens in range(1, upper_border_tens + 1):
        for nums in range(1, upper_border_nums + 1):
            if nums % 2 == 0 and hundreds % 2 == 0:
                if tens in list1:
                    print(f"{hundreds} {tens} {nums}")

