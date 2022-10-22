def fill_the_box(height: int, lenght: int, width: int, *args):
    args = [*args]
    size = height * lenght * width
    for _ in range(len(args)):
        if args[0] == 'Finish':
            args.pop(0)
            break
        if size < args[0]:
            args[0] -= size
            size = 0
            args.remove('Finish')
            break
        size -= args[0]
        args.pop(0)

    if size == 0:
        return f'No more free space! You have {sum(args)} more cubes.'
    else:
        return f'There is free space in the box. You could put {size} more cubes.'

