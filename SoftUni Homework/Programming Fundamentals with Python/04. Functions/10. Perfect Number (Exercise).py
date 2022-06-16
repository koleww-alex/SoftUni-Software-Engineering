def is_perfect(number):
    number_sum = 0
    for i in range(1, number):
        if number % i == 0:
            number_sum += i
    if number == number_sum:
        return True


positive_number = int(input())

perfect_number = is_perfect(positive_number)

if perfect_number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
