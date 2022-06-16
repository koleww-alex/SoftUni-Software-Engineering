number_chicken_menu = int(input())
number_fish_menu = int(input())
number_vegetarian_menu = int(input())
chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
order_without_desert = (number_chicken_menu * chicken_menu) + (number_fish_menu * fish_menu) + \
                       (number_vegetarian_menu * vegetarian_menu)
desert = order_without_desert * 0.2
take_away = 2.5
final_price = order_without_desert + desert + take_away
print(final_price)
