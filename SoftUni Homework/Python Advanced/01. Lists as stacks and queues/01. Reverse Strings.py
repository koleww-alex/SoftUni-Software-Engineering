string = list(input())
# reversed_string = string[::-1]
reversed_list = []
while string:
    reversed_list.append(string.pop())
print(''.join(reversed_list))
