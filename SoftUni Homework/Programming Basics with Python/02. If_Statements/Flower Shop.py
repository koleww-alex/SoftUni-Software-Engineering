number_magnolii = int(input())
number_ziumbiuli = int(input())
number_rozi = int(input())
number_kaktusi = int(input())
gift_price = float(input())
from math import floor, ceil

magnolii = 3.25
ziumbiuli = 4
rozi = 3.50
kaktusi = 8

raw_profit = (number_magnolii * magnolii) + (number_ziumbiuli * ziumbiuli) + (number_rozi * rozi) + (number_kaktusi * kaktusi)
tax = raw_profit * 0.05
profit = raw_profit - tax

if profit >= gift_price:
    print(f"She is left with {floor(profit - gift_price)} leva.")
else:
    print(f"She will have to borrow {ceil(gift_price - profit)} leva.")
