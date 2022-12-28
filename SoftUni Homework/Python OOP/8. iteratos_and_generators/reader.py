def read_next(*args):

    for element in args:
        for ch in element:
            yield ch
