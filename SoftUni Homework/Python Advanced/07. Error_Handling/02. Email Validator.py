import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


name_pattern = r'[\w\.\-]+'
email_pattern = r'([\w\.\-]+)(\@[a-z]+)(\.[a-z]+)'
command = input()
valid_domains = ['.bg', '.net', '.com', '.org']
while command != 'End':
    email = command
    name = re.search(name_pattern, email)
    cnt = email.count('@')
    if len(name.group()) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')

    elif cnt <= 0:
        raise MustContainAtSymbolError('Email must contain @')

    elif cnt > 1:
        raise MoreThanOneAtSymbolError('Email must not contain more than one @')

    email_info = re.search(email_pattern, email)
    domain = email_info[3]

    if domain not in valid_domains:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    print('Email is valid')
    command = input()
