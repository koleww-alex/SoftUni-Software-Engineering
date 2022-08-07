items = input().split()

dictionary = {items[i]: int(items[i + 1]) for i in range(0, len(items), 2)}

# dictionary = {}
# for i in range(0, len(items), 2):
#     key, value = items[i], items[i + 1]
#     dictionary[key] = int(value)

print(dictionary)
