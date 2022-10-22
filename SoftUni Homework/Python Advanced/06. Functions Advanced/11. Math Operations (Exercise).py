def math_operations(*args, **kwargs):
    result = ''
    cnt = 0
    for num in args:
        cnt += 1
        if cnt == 1:
            kwargs['a'] += num

        elif cnt == 2:
            kwargs['s'] -= num

        elif cnt == 3:
            if num == 0 or kwargs['d'] == 0:
                continue
            kwargs['d'] /= num

        elif cnt == 4:
            kwargs['m'] *= num
            cnt = 0

    for key, val in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])):
        result += f'{key}: {val:.1f}' + '\n'

    return result
