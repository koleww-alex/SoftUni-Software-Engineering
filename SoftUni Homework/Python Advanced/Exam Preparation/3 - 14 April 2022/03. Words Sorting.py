def words_sorting(*args):
    words = {}
    output = []
    for key in args:
        words[key] = 0
        for ch in key:
            words[key] += ord(ch)

    if sum(words.values()) % 2 == 0:
        for key, val in sorted(words.items(), key=lambda x: x[0]):
            output.append(f'{key} - {val}')
    else:
        for key, val in sorted(words.items(), key=lambda x: -x[1]):
            output.append(f'{key} - {val}')

    return '\n'.join(output)

