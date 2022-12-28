def vowel_filter(function):
    def wrapper():
        vowels = ['a', 'y', 'o', 'u', 'e', 'i']
        result = function()
        return [x for x in result if x.lower() in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
