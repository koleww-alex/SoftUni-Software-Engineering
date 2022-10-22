def func_executor(*args):
    result = ''
    for arg in args:
        result += f'{arg[0].__name__} - {arg[0](*arg[1])}' + '\n'

    return result
