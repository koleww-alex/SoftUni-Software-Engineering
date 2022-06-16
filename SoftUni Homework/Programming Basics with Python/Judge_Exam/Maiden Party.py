price_girl_party = float(input())

number_of_love_letters = int(input())
number_of_roses = int(input())
number_of_key_holders = int(input())
number_of_cartoons = int(input())
number_of_surprise_luck = int(input())

price_love_letters = number_of_love_letters * 0.60
price_roses = number_of_roses * 7.20
price_key_holders = number_of_key_holders * 3.60
price_cartoons = number_of_cartoons * 18.20
price_surprise_luck = number_of_surprise_luck * 22

total_numbers = number_of_love_letters + number_of_roses + number_of_key_holders + number_of_cartoons + number_of_surprise_luck

total_price = price_love_letters + price_roses + price_key_holders + price_cartoons + price_surprise_luck

if total_numbers >= 25:
    total_price -= total_price * 0.35

final_price = total_price - (total_price * 0.1)

diff = abs(final_price - price_girl_party)

if final_price >= price_girl_party:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
