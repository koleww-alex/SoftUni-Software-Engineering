def type_check(type):
    def decorator(function):
        def wrapper(type_to_check):
            if isinstance(type_to_check, type):
                result = function(type_to_check)
                return result

            return f'Bad Type'

        return wrapper

    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
