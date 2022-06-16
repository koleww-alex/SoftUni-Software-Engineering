def function(num_one, num_two, num_three):
    multiplication_type = ""
    if num_one < 0 or num_two < 0 or num_three < 0:
        multiplication_type = "negative"
    elif num_one == 0 or num_two == 0 or num_three == 0:
        multiplication_type = "zero"
    elif num_one > 0 and num_two > 0 and num_three > 0:
        multiplication_type = "positive"

    return multiplication_type


number_one = int(input())
number_two = int(input())
number_three = int(input())

print(function(number_one, number_two, number_three))
