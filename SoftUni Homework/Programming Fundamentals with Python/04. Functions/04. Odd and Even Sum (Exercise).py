def odd_even_sum(num):
    even_sum = 0
    odd_sum = 0
    for element in number:
        current_number = int(element)
        if current_number % 2 == 0:
            even_sum += current_number
        else:
            odd_sum += current_number
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()

print(odd_even_sum(number))
