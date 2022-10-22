def shopping_list(budget: int, **kwargs):
    basket_size = 5
    bought_items = {}
    output = []
    if budget < 100:
        return 'You do not have enough budget.'

    for key, val in kwargs.items():
        price = val[0] * val[1]
        if len(bought_items) == basket_size:
            break
        if budget >= price:
            bought_items[key] = price
            budget -= price

    for key, val in bought_items.items():
        output.append(f'You bought {key} for {val:.2f} leva.')

    return '\n'.join(output)


