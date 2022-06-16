total_energy = 100
total_coins = 100

events = input().split("|")

is_bakery_closed = False

for event in events:
    event_info = event.split("-")

    event_type = event_info[0]
    event_value = int(event_info[1])

    if event_type == "rest":
        current_energy = total_energy
        total_energy += event_value

        if total_energy > 100:
            total_energy = 100

        gained = total_energy - current_energy
        print(f"You gained {gained} energy.")
        print(f"Current energy: {total_energy}.")

    elif event_type == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50
            print("You had to rest!")

    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {event_type}.")
        else:
            print(f"Closed! Cannot afford {event_type}.")
            is_bakery_closed = True
            break

if not is_bakery_closed:
    print(f"Day completed!\n"
          f"Coins: {total_coins}\n"
          f"Energy: {total_energy}")





