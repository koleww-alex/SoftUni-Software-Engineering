price_for_one_square_meter = 7.61
square_meters_to_be_landscaped = float(input())
price_before_discount = square_meters_to_be_landscaped * 7.61
discount = price_before_discount * 0.18
final_price = price_before_discount - discount
print(f"The final price is: {final_price} lv. "
      f"The discount is: {discount} lv.")
