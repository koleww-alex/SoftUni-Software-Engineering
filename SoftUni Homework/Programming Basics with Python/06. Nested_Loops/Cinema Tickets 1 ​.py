command = input()

is_statistic_done = False

r1 = 0
r2 = 0
r3 = 0

p1 = 0
p2 = 0
p3 = 0

people = 0
tickets = 0
total_tickets = 0
percent_filling_the_hall = 0

while True:
    spaces_in_movie_hall = int(input())
    command_2 = input()
    while command_2 != "End":
        if command_2 == "Finish":
            is_statistic_done = True
            break

        if command_2 == "student":
            r1 += 1
            people += 1
        elif command_2 == "standard":
            r2 += 1
            people += 1
        else:
            r3 += 1
            people += 1

        total_tickets = r1 + r2 + r3

        tickets = r1 + r2 + r3
        p1 = (r1 / tickets) * 100
        p2 = (r2 / tickets) * 100
        p3 = (r3 / tickets) * 100

        percent_filling_the_hall = (people / spaces_in_movie_hall) * 100

        command_2 = input()

    print(f"{command} - {percent_filling_the_hall:.2f}% full.")

    tickets = 0
    people = 0
    if is_statistic_done:
        break

    command = input()

print(f"Total tickets: {total_tickets}\n"
      f"{p1:.2f}% student tickets.\n"
      f"{p2:.2f}% standard tickets.\n"
      f"{p3:.2f}% kids tickets.")
