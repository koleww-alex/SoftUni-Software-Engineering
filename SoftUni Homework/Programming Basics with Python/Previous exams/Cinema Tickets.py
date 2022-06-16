movie = input()
number_free_spaces = int(input())
ticket_type = input()
used_spaces = 0

r1 = 0
r2 = 0
r3 = 0
percent_used = 0

p1 = 0
p2 = 0
p3 = 0

while movie != "Finish":

    while ticket_type != "End":

        if ticket_type == "student":
            r1 += 1
        elif ticket_type == "standard":
            r2 += 1
        else:
            r3 += 1

        used_spaces = r1 + r2 + r3

        p1 = (r1 / number_free_spaces) * 100
        p2 = (r2 / number_free_spaces) * 100
        p3 = (r3 / number_free_spaces) * 100

        percent_used = (used_spaces / number_free_spaces) * 100

        if used_spaces > number_free_spaces:
            break

        ticket_type = input()

    print(f"{movie} - {percent_used}% full.")

    movie = input()

print(f"Total tickets: {used_spaces}"
      f"{p1}% student tickets.\n"
      f"{p2}% standard tickets.\n"
      f"{p3}% kids tickets.")


# Unfinished !!!!!
