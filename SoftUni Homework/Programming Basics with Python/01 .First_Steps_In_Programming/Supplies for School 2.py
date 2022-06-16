packet_of_pens = int(input())
packet_of_markers = int(input())
packet_of_detergent = int(input())
percent_discount = int(input()) / 100
pens = 5.80
markers = 7.20
detergent = 1.20
price_before_discount = (packet_of_pens * pens) + (packet_of_markers * markers) + (packet_of_detergent * detergent)
discount = price_before_discount * percent_discount
final_price = price_before_discount - discount
print(final_price)
