def create_sequence(n):
    result = [0, 1]
    for i in range(2, n):
        next_num = result[-2] + result[-1]
        result.append(next_num)
    return result
