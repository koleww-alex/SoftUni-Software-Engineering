def password_validator(current_password):
    digits_cnt = 0
    password_is_valid = True
    if not 6 <= len(current_password) <= 10:
        print("Password must be between 6 and 10 characters")
        password_is_valid = False

    if not current_password.isalnum():
        print("Password must consist only of letters and digits")
        password_is_valid = False

    for element in current_password:
        if element.isdigit():
            digits_cnt += 1

    if not digits_cnt >= 2:
        print("Password must have at least 2 digits")
        password_is_valid = False

    return password_is_valid


password = input()

is_valid = password_validator(password)

if is_valid:
    print("Password is valid")

