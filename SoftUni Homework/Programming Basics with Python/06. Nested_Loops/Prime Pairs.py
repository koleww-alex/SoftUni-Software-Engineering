start_first_pair = int(input())
start_second_pair = int(input())

diff_first_pair = int(input())
diff_second_pair = int(input())

end_first_pair = start_first_pair + diff_first_pair
end_second_pair = start_second_pair + diff_second_pair

is_this_non_prime_x1 = False
is_this_non_prime_x2 = False

for x1 in range(start_first_pair, end_first_pair + 1):
    for x2 in range(start_second_pair, end_second_pair + 1):
        for i in range(start_first_pair, x1):
            if x1 % i == 0:
                is_this_non_prime_x1 = True
            if not is_this_non_prime_x1:
                for y in range(start_second_pair, x2):
                    if x2 % y == 0:
                        is_this_non_prime_x2 = True
                    if not is_this_non_prime_x2:
                        if x1 == x2:
                            continue
                        print(f"{x1}{x2}", end=" ")

# Unfinished
