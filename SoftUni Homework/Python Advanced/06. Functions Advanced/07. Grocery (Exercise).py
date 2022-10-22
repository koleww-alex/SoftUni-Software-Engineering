def grocery_store(**kwargs):
    result = ''
    for key, val in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
        result += f'{key}: {val}' + '\n'

    return result
