def separator_nums(string: str):
    return "".join(ch for ch in string if ch.isdigit())


def separator_chr(string: str):
    return "".join(ch for ch in string if ch.isalpha())


def separator_symbols(string: str):
    return "".join(ch for ch in string if not ch.isalnum())


word = input()
print(separator_nums(word))
print(separator_chr(word))
print(separator_symbols(word))
