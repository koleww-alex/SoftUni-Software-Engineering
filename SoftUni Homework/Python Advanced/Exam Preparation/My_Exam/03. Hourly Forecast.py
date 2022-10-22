def forecast(*args):
    weather_info = {}
    order = ['Sunny', 'Cloudy', 'Rainy']
    output = []
    for arg in args:
        location, weather = arg
        weather_info[location] = weather

    for key, val in sorted(weather_info.items(), key=lambda x: (order.index(x[1]), x[0])):
        output.extend([f'{key} - {val}'])

    return '\n'.join(output)

