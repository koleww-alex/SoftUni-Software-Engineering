movie = input()

student = 0
standard = 0
kid = 0
total_tickets = 0

while movie != "Finish":
    free_spaces = int(input())
    busy_seats = 0
    for _ in range(1, free_spaces + 1):
        ticket = input()

        if ticket == "student":
            student += 1
        elif ticket == "standard":
            standard += 1
        elif ticket == "kid":
            kid += 1
        elif ticket == "End":
            break

        busy_seats += 1
    percent_room = (busy_seats / free_spaces) * 100
    total_tickets = student + standard + kid

    print(f"{movie} - {percent_room:.2f}% full.")

    movie = input()

print(f"Total tickets: {total_tickets}\n"
      f"{(student / total_tickets) * 100:.2f}% student tickets.\n"
      f"{(standard / total_tickets) * 100:.2f}% standard tickets.\n"
      f"{(kid / total_tickets) * 100:.2f}% kids tickets.")

