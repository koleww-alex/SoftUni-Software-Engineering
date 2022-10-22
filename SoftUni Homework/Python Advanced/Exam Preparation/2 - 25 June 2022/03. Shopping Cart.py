def shopping_cart(*args):
    cnt = 0
    products_limits = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2,
    }
    cart = {
        'Soup': [],
        'Pizza': [],
        'Dessert': [],
    }
    output = []
    for items in args:
        if items == 'Stop':
            break

        key, val = items
        if products_limits[key] > 0 and val not in cart[key]:
            products_limits[key] -= 1
            cart[key].append(val)
        cnt += 1

    for key, val in sorted(cart.items(), key=lambda x: (-len(x[1]), x[0])):
        output.append(f'{key}:')
        if val:
            output.append('\n'.join(f' - {x}' for x in sorted(val)))

    if cnt > 0:
        return '\n'.join(output)
    return 'No products in the cart!'

