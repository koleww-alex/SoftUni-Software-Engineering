def rectangle(length, width):
    if isinstance(length, int) and isinstance(width, int):

        def area():
            return f'Rectangle area: {length * width}'

        def perimeter():
            return f'Rectangle perimeter: {2 * length + 2 * width}'

        return area() + '\n' + perimeter()
    else:
        return 'Enter valid values!'

