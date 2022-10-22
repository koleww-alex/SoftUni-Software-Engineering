def sorting_cheeses(**kwargs):
    result = ''
    for key, value in sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0])):
        value = sorted(value, reverse=True)
        result += key + '\n'
        result += '\n'.join(str(x) for x in value) + '\n'

    return result
