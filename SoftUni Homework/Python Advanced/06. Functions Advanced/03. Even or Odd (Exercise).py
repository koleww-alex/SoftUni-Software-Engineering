def even_odd(*args):
    command = args[-1]

    def even():
        return [x for x in args[:-1] if x % 2 == 0]

    def odd():
        return [x for x in args[:-1] if x % 2 != 0]

    if command == 'even':
        return even()
    else:
        return odd()
