def numbers_searching(*args):
    output = []
    duplicates = sorted(set([x for x in args if args.count(x) > 1]))
    numbers = sorted(set(args))
    for num in range(min(numbers), max(numbers) + 1):
        if num not in numbers:
            output.append(num)

    output.append(duplicates)

    return output
