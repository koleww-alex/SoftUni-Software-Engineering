number_detergent_bottles = int(input())
command = input()
total_ml = number_detergent_bottles * 750
number_plates = 0
number_pot = 0
days_cnt = 0
total_ml_used = 0
detergent_not_enough = False

while command != "End":
    days_cnt += 1
    command = int(command)
    if days_cnt % 3 == 0:
        number_pot += command
    else:
        number_plates += command

    ml_used_plates = number_plates * 5
    ml_used_pots = number_pot * 15
    total_ml_used = ml_used_plates + ml_used_pots

    if total_ml < total_ml_used:
        detergent_not_enough = True
        break
    command = input()


if detergent_not_enough:
    detergent_needed = total_ml_used - total_ml
    print(f"Not enough detergent, {detergent_needed} ml. more necessary!")

else:
    detergent_left = total_ml - total_ml_used
    print(f"Detergent was enough!\n"
          f"{number_plates} dishes and {number_pot} pots were washed.\n"
          f"Leftover detergent {detergent_left} ml.")
