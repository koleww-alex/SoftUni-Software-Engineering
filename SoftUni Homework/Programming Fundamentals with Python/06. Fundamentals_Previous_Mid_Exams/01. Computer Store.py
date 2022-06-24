prices_without_taxes = input()
total_price_without_taxes = 0
total_price_with_taxes = 0
while prices_without_taxes != "special" and prices_without_taxes != "regular":
    if float(prices_without_taxes) < 0:
        print("Invalid price!")
    else:
        total_price_without_taxes += float(prices_without_taxes)

    prices_without_taxes = input()

total_price_with_taxes = total_price_without_taxes + (total_price_without_taxes * 0.2)

taxes = total_price_with_taxes - total_price_without_taxes

if prices_without_taxes == "special":
    total_price_with_taxes -= total_price_with_taxes * 0.1


if total_price_with_taxes == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price_without_taxes:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          f"-----------\n"
          f"Total price: {total_price_with_taxes:.2f}$")
