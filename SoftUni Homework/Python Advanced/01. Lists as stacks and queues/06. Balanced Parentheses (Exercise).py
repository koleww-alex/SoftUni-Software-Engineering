parentheses = input()
indices = []
result = []
for i in range(len(parentheses)):
    if parentheses[i] == '(' or parentheses[i] == '[' or parentheses[i] == '{':
        indices.append(i)
    elif parentheses[i] == ')' or parentheses[i] == ']' or parentheses[i] == '}':
        if indices:
            last_opening_bracket = indices.pop()
            if parentheses[last_opening_bracket] + parentheses[i] in ['()', '[]', '{}']:
                result.append(True)
            else:
                result.append(False)
                break
        else:
            result.append(False)
            break
if all(result):
    print('YES')
else:
    print('NO')
