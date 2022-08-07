def correct_lenght(username: str):
    if 3 <= len(username) <= 16:
        return True
    return False


def correct_symbols(username: str):
    is_valid = False
    for ch in username:
        if ch.isalnum() or ch == "-" or ch == "_":
            is_valid = True
        else:
            return False
    return is_valid


def no_redundant_spaces(username: str):
    if " " in username:
        return False
    return True


def name_is_valid(list_of_usernames: list):
    for name in list_of_usernames:
        if correct_lenght(name) and correct_symbols(name) and no_redundant_spaces(name):
            print(name)


usernames = input().split(", ")

name_is_valid(usernames)
