n = int(input())
word = input()

standard_list = []

for _ in range(1, n + 1):
    current_word = input()
    standard_list.append(current_word)

print(standard_list)

for i in range(len(standard_list) - 1, - 1, - 1):
    element = standard_list[i]
    if word not in element:
        standard_list.remove(element)

print(standard_list)