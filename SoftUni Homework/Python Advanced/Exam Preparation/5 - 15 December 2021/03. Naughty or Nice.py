def naughty_or_nice_list(*args, **kwargs):
    all_kids = []
    nice_kids = []
    bad_kids = []
    not_found_kids = []
    output = []
    for arg in args:
        if isinstance(arg, list):
            for t in arg:
                val, name = t
                all_kids.append(name)
                all_kids.append(val)
        else:
            number, behaviour = arg.split('-')

            if all_kids.count(int(number)) == 1:
                kid = all_kids[all_kids.index(int(number)) - 1]

                if behaviour == 'Nice':
                    nice_kids.append(kid)
                else:
                    bad_kids.append(kid)
                all_kids.pop(all_kids.index(kid) + 1)
                all_kids.remove(kid)

    for kid, behaviour in kwargs.items():
        if all_kids.count(kid) == 1:
            if behaviour == 'Nice':
                nice_kids.append(kid)
            else:
                bad_kids.append(kid)
            all_kids.pop(all_kids.index(kid) + 1)
            all_kids.remove(kid)

    for i in range(0, len(all_kids), 2):
        not_found_kids.append(all_kids[i])

    if nice_kids:
        output.append(f"Nice: {', '.join(str(x) for x in nice_kids)}")

    if bad_kids:
        output.append(f"Naughty: {', '.join(str(x) for x in bad_kids)}")

    if not_found_kids:
        output.append(f"Not found: {', '.join(str(x) for x in not_found_kids)}")

    return '\n'.join(output)


