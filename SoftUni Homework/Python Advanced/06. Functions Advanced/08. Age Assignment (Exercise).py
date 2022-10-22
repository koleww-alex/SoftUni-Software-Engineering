def age_assignment(*args, **kwargs):
    info = {}
    result = ''
    for name in args:
        for key in kwargs.keys():
            if name.startswith(key):
                info[name] = kwargs[key]

    for key, val in sorted(info.items(), key=lambda x: x[0]):
        result += f'{key} is {val} years old.' + '\n'
    return result
