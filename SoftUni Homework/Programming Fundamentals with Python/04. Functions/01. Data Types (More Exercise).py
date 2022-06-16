def function(type_element, element):
    result = ""
    if type_element == "int":
        element = int(element)
        result = element * 2
    elif type_element == "real":
        element = float(element)
        result = f"{element * 1.5:.2f}"
    elif type_element == "string":
        result = f"${element}$"

    return result


type_of_element = input()
current_element = input()

print(function(type_of_element, current_element))
