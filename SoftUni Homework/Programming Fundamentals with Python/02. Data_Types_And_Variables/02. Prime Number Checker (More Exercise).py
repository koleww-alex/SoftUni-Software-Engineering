number = int(input())
is_non_prime = False
for num in range(2, number):

    if number % num == 0:
        is_non_prime = True

if not is_non_prime:
    print("True")
else:
    print("False")
