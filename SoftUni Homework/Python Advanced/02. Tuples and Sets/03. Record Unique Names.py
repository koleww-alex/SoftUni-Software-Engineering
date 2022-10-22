number_of_iterations = int(input())
# Using list and convert to set

list_of_names = []
for _ in range(number_of_iterations):
    name = input()
    list_of_names.append(name)

unique_names = set(list_of_names)
print('\n'.join(unique_names))

# Instantly using set

unique_names = set()
for _ in range(number_of_iterations):
    name = input()
    unique_names.add(name)
print('\n'.join(unique_names))
