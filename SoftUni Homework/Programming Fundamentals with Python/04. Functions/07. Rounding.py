def rounder(list):
    for float_num in list_of_floats:
        list_of_integers.append(round(float_num))

    return list_of_integers


list_of_floats = list(map(float, input().split()))
list_of_integers = []

print(rounder(list_of_floats))
