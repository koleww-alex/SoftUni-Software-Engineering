def concatenate(*args, **kwargs):
    result = ''
    for arg in args:
        result += arg

    for key in kwargs.keys():
        if key in result:
            result = result.replace(key, kwargs[key])

    return result
