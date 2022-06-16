budget = float(input())
number_gpu = int(input())
number_cpu = int(input())
number_ram = int(input())
gpu = 250
cpu = (gpu * number_gpu) * 0.35
ram = (gpu * number_gpu) * 0.1
final_price = (number_gpu * gpu) + (number_cpu * cpu) + (number_ram * ram)

if number_gpu > number_cpu:
    discount = final_price * 0.15
    final_price = final_price - discount

if budget >= final_price:
    print(f"You have {budget - final_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {final_price - budget:.2f} leva more!")

