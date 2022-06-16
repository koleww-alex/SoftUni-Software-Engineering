list_of_items = input().split("|")
budget = int(input())

bought_items = []

for item in list_of_items:
    list_info = item.split("->")

    item_info = list_info[0]
    item_price = float(list_info[1])

    if item_info == "Clothes":
        if item_price <= 50.00 and budget >= item_price:
            budget -= item_price
            bought_items.append(item_price)

    elif item_info == "Shoes":
        if item_price <= 35.00 and budget >= item_price:
            budget -= item_price
            bought_items.append(item_price)
    elif item_info == "Accessories":
        if item_price <= 20.50 and budget >= item_price:
            budget -= item_price
            bought_items.append(item_price)

total_bought_items_price = sum(bought_items)

sold_price_items = []

for price in bought_items:
    new_price = price + (price * 0.4)
    sold_price_items.append(new_price)

total_sold_items_price = sum(sold_price_items)

profit = total_sold_items_price - total_bought_items_price

total_budget = total_sold_items_price + budget

format_bought_items = []

for sold_item in sold_price_items:
    format_bought_items.append(f"{sold_item:.2f}")

print(" ".join(format_bought_items))
print(f"Profit: {profit:.2f}")

if total_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
