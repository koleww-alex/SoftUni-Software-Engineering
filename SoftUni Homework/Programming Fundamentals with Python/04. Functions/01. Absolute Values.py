def abs_value(number: float):
    result = [abs(number) for number in list_of_integers]
    return result


list_of_integers = list(map(float, input().split()))

print(abs_value(list_of_integers))
