def start_spring(**kwargs):
    spring = {}
    output = []
    for val, key in kwargs.items():
        if key not in spring:
            spring[key] = []
        spring[key].append(val)

    for key, val in sorted(spring.items(), key=lambda x: (-len(x[1]), x[0])):
        output.append(f'{key}:')
        output.append('\n'.join(f'-{item}' for item in sorted(val)))

    return '\n'.join(output)
