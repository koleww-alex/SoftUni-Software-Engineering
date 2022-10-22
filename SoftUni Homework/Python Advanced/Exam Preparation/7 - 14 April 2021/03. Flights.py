def flights(*args):
    flights_check = {}
    for i in range(0, len(args), 2):
        flight = args[i]
        if flight == 'Finish':
            break
        if flight not in flights_check:
            flights_check[flight] = 0

        passengers = args[i + 1]
        if passengers == 'Finish':
            break
        flights_check[flight] += passengers

    return flights_check


