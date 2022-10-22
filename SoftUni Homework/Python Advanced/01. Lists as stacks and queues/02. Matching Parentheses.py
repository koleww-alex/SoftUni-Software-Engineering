expression = input()
list_of_indices = []
for i in range(len(expression)):
    if expression[i] == '(':
        list_of_indices.append(i)
    elif expression[i] == ')':
        last_opening_bracket = list_of_indices.pop()
        print(expression[last_opening_bracket:i + 1])
