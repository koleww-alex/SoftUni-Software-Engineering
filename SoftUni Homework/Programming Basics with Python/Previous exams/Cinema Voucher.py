voucher_price = int(input())
command = input()
number_tickets = 0
others = 0
price = 0

while command != "End":
    lenght_movie = len(command)

    if lenght_movie > 8:
        first_ch = command[0]
        second_ch = command[1]
        price += ord(first_ch)
        price += ord(second_ch)
        if price > voucher_price:
            break
        number_tickets += 1
    else:
        first_ch = command[0]
        price += ord(first_ch)
        if price > voucher_price:
            break
        others += 1

    command = input()

print(f"{number_tickets}\n"
      f"{others}")

