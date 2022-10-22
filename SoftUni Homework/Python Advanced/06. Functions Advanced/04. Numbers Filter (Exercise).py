def even_odd_filter(**kwargs):
    for key, val in kwargs.items():
        if key == 'even':
            kwargs[key] = [x for x in val if x % 2 == 0]
        else:
            kwargs[key] = [x for x in val if x % 2 != 0]

    return kwargs
