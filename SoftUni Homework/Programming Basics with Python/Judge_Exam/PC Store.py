price_cpu_before_discount_usd = float(input())
price_gpu_before_discount_usd = float(input())
price_ram_usd = float(input())
number_of_ram = int(input())
percent_discount = float(input())

cpu_lv = price_cpu_before_discount_usd * 1.57
gpu_lv = price_gpu_before_discount_usd * 1.57
ram_lv = price_ram_usd * 1.57

final_cpu_lv = cpu_lv - (cpu_lv * percent_discount)
final_gpu_lv = gpu_lv - (gpu_lv * percent_discount)
total_ram = ram_lv * number_of_ram


total_sum_lv = final_cpu_lv + final_gpu_lv + total_ram

print(f"Money needed - {total_sum_lv:.2f} leva.")
