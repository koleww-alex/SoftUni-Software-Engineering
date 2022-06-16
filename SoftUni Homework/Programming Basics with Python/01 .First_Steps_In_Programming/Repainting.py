needed_plastic_bag = int(input())
needed_paint = int(input())
needed_thinner = int(input())
needed_hours = int(input())
protective_plastic_bag = 1.5
paint = 14.5
paint_thinner = 5
price_before_extras = (needed_plastic_bag * protective_plastic_bag) + (needed_paint * paint) + \
                      (needed_thinner * paint_thinner)
plastic_bag = 0.4
price_after_extras = price_before_extras + (0.1 * needed_paint * paint) + (2 * protective_plastic_bag) + plastic_bag
price_for_work_per_hour = price_after_extras * 0.3
work_price = needed_hours * price_for_work_per_hour
final_price = price_after_extras + work_price
print(final_price)
